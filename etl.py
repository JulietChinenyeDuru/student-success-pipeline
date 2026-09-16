from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, round as spark_round

spark = SparkSession.builder.appName("StudentSuccessPipeline").getOrCreate()

# --- EXTRACT ---
df = spark.read.csv("data/students_dropout_academic_success.csv", header=True, inferSchema=True)
print("Raw row count:", df.count())

# --- CLEAN: standardize column names (remove spaces, apostrophes, parentheses) ---
for old_name in df.columns:
    new_name = (old_name.strip()
                .replace(" ", "_")
                .replace("'", "")
                .replace("(", "")
                .replace(")", "")
                .replace("/", "_")
                .lower())
    df = df.withColumnRenamed(old_name, new_name)

print("Cleaned columns:", df.columns)

# --- CLEAN: drop rows missing the target (can't use them for analysis) ---
df = df.na.drop(subset=["target"])

# --- TRANSFORM: average semester grade across 1st and 2nd sem ---
df = df.withColumn(
    "avg_grade",
    spark_round(
        (col("curricular_units_1st_sem_grade") + col("curricular_units_2nd_sem_grade")) / 2, 2
    )
)

# --- TRANSFORM: simple dropout risk score (lower grade + more failed/unevaluated units = higher risk) ---
df = df.withColumn(
    "risk_score",
    when(col("avg_grade") < 10, 3)          # high risk
    .when(col("avg_grade") < 13, 2)         # medium risk
    .otherwise(1)                            # low risk
)

# --- LOAD/AGGREGATE: summary by target outcome ---
summary = df.groupBy("target").agg(
    {"avg_grade": "avg", "risk_score": "avg"}
).withColumnRenamed("avg(avg_grade)", "mean_grade") \
 .withColumnRenamed("avg(risk_score)", "mean_risk_score")

print("=== Summary by outcome ===")
summary.show()

print("=== Sample transformed rows ===")
df.select("target", "avg_grade", "risk_score").show(10)

print("Final row count after cleaning:", df.count())

spark.stop()

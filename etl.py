from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, round as spark_round

spark = SparkSession.builder.appName("StudentSuccessPipeline").getOrCreate()

df = spark.read.csv("data/students_dropout_academic_success.csv", header=True, inferSchema=True)
print("Raw row count:", df.count())

for old_name in df.columns:
    new_name = (old_name.strip()
                .replace(" ", "_")
                .replace("'", "")
                .replace("(", "")
                .replace(")", "")
                .replace("/", "_")
                .lower())
    df = df.withColumnRenamed(old_name, new_name)

df = df.na.drop(subset=["target"])

df = df.withColumn(
    "avg_grade",
    spark_round(
        (col("curricular_units_1st_sem_grade") + col("curricular_units_2nd_sem_grade")) / 2, 2
    )
)

df = df.withColumn(
    "risk_score",
    when(col("avg_grade") < 10, 3)
    .when(col("avg_grade") < 13, 2)
    .otherwise(1)
)

summary = df.groupBy("target").agg(
    {"avg_grade": "avg", "risk_score": "avg"}
).withColumnRenamed("avg(avg_grade)", "mean_grade") \
 .withColumnRenamed("avg(risk_score)", "mean_risk_score")

print("=== Summary by outcome ===")
summary.show()

df.select("target", "avg_grade", "risk_score").toPandas().to_csv("output/results.csv", index=False)
summary.toPandas().to_csv("output/summary.csv", index=False)
print("Saved output files for dashboard.")

spark.stop()

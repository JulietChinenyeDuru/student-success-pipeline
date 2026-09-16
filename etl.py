from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StudentSuccessPipeline").getOrCreate()
df = spark.read.csv("data/students_dropout_academic_success.csv", header=True, inferSchema=True)
df.show(5)
print("Total rows:", df.count())

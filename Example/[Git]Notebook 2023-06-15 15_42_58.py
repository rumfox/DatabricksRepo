# Databricks notebook source
# MAGIC %md
# MAGIC # Git Repository Test Notebook
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "GIT Repository Test"

# COMMAND ----------

from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [
    {"name": "John", "age": 25, "city": "New York"},
    {"name": "Alice", "age": 30, "city": "London"},
    {"name": "Bob", "age": 35, "city": "Paris"}
]

# Create DataFrame
df = spark.createDataFrame(data)

# Show DataFrame
df.show()


# COMMAND ----------

from pyspark.sql.functions import substring;
from pyspark.sql.functions import col

# df.select(substring(col("string"),start, length))

# Extract substring from 'name' column
df = df.withColumn("substring", col("name").substr(1, 4))

df.show()

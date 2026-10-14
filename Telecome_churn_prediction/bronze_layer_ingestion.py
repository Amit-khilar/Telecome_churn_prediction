# Databricks notebook source
df=spark.read.csv('/Volumes/churn_catalog/bronze/churn_volume/sttm_source_data.csv',header=True)

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

# COMMAND ----------

df = df.withColumn("_ingestion_timestamp", current_timestamp())

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("churn_catalog.bronze.customer_raw") 
# Databricks notebook source
from pyspark.sql.functions import when, col, current_timestamp

# COMMAND ----------

df_silver = spark.table("churn_catalog.silver.customer_clean")
display(df_silver)

# COMMAND ----------

df_gold = (df_silver
    .withColumn("tenure_bucket",
        when(col("tenure") <= 12, "0-12mo")
        .when(col("tenure") <= 24, "13-24mo")
        .otherwise("25mo+"))
    .withColumn("churn_flag", when(col("Churn") == True, 1).otherwise(0))
    .withColumn("_ingestion_timestamp", current_timestamp())
)
df_gold.write.format("delta").mode("overwrite").saveAsTable("churn_catalog.gold.customer_features")

# COMMAND ----------

display(df_gold)

# COMMAND ----------

df_gold_report=df_gold.groupby("Contract","tenure_bucket").agg(
    {"churn_flag":"avg"}
    ).withColumnRenamed("avg(churn_flag)","churn_rate")
display(df_gold_report)


# COMMAND ----------

df_gold_report.write.format("delta").mode("overwrite").saveAsTable("churn_catalog.gold.churn_rate_by_segment")


# COMMAND ----------


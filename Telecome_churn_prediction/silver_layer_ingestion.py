# Databricks notebook source
from pyspark.sql.functions import col, when, trim, expr, current_timestamp, lower

# COMMAND ----------

df_bronze=spark.table("churn_catalog.bronze.customer_raw")

# COMMAND ----------

display(df_bronze)

# COMMAND ----------

df_silver = (df_bronze
    .withColumn("TotalCharges", expr("try_cast(TotalCharges as double)"))
    .withColumn("MonthlyCharges", col("MonthlyCharges").cast("double"))
    .withColumn("tenure", col("tenure").cast("int"))
    .withColumn("Churn", when(col("Churn") == "Yes", True).otherwise(False))
    .dropDuplicates(["customerID"])
    .filter(col("customerID").isNotNull())
)

# COMMAND ----------

df_silver = df_silver.withColumn("_ingestion_timestamp", current_timestamp())

# COMMAND ----------

df_silver=df_silver.withColumn("Contract",when (col("Contract")=="MONTH-TO-MONTH","month-to-month").otherwise(col("Contract"))) 

# COMMAND ----------

df_silver=df_silver.withColumn("Contract",when (col("Contract")=="Month-to-month ","month-to-month").otherwise(col("Contract"))) 

# COMMAND ----------

df_silver=df_silver.withColumn("Contract",trim(lower(col("Contract"))))

# COMMAND ----------

df_silver.select("Contract").distinct().display()

# COMMAND ----------

display(df_silver)

# COMMAND ----------

df_silver.write.format("delta").mode("overwrite").saveAsTable("churn_catalog.silver.customer_clean") 
# Databricks notebook source
# MAGIC %sql
# MAGIC create catalog if not exists churn_catalog;
# MAGIC create schema if not exists churn_catalog.bronze;
# MAGIC create schema if not exists churn_catalog.silver;
# MAGIC create schema if not exists churn_catalog.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume if not exists churn_catalog.bronze.churn_volume
# MAGIC
# Telecom Customer Churn Prediction Using Medallion Architecture

## Project Overview

This project focuses on building a data engineering and analytics pipeline for Telecom Customer Churn Prediction using **PySpark, Databricks, and Medallion Architecture**.

Customer churn occurs when customers stop using a company's services. Predicting churn helps telecom companies identify customers who are likely to leave and take proactive steps to improve customer retention.

The project follows the Medallion Architecture approach, organizing data into three layers: **Bronze, Silver, and Gold**. Each layer improves data quality and prepares the data for downstream analytics and churn prediction.

## Project Objectives

- Build a structured data pipeline using Medallion Architecture.
- Ingest raw telecom customer data into the Bronze layer.
- Clean, validate, and transform data in the Silver layer.
- Create analytics-ready datasets in the Gold layer.
- Prepare customer data for churn analysis and machine learning.
- Support business decisions aimed at reducing customer churn.

## Architecture

The project follows the Medallion Architecture pattern.

**Data Source → Bronze → Silver → Gold → Churn Analysis / Machine Learning**

### 1. Bronze Layer — Raw Data Ingestion

The Bronze layer stores raw data ingested from the source files.

Key activities:
- Read source data into Databricks using PySpark.
- Preserve raw records for traceability.
- Add ingestion metadata where required.
- Store the ingested data in Delta tables.

### 2. Silver Layer — Data Cleaning and Transformation

The Silver layer contains cleaned and validated data.

Key activities:
- Handle missing and invalid values.
- Remove duplicate records where appropriate.
- Standardize column values and data formats.
- Apply data type conversions.
- Validate customer and business-related fields.
- Prepare consistent data for downstream analysis.

### 3. Gold Layer — Business-Ready Data

The Gold layer contains curated datasets designed for business analysis and machine learning.

Key activities:
- Create analytics-ready customer datasets.
- Prepare relevant features for churn analysis.
- Organize transformed data for downstream reporting and prediction.
- Support the identification of customers who may be at risk of leaving.

## 🛠️ Technologies Used

- **Python** — Programming language
- **PySpark** — Distributed data processing and transformation
- **Databricks** — Data engineering and lakehouse platform
- **Delta Lake** — Reliable storage for lakehouse tables
- **Medallion Architecture** — Layered data processing approach
- **Machine Learning** — Customer churn prediction, where implemented

## Project Workflow

1. Ingest raw telecom data into the Bronze layer.
2. Clean and validate the data in the Silver layer.
3. Transform and prepare business-ready datasets in the Gold layer.
4. Prepare relevant customer features for churn analysis.
5. Use the prepared data for churn prediction and business insights, according to the implemented model.

## Business Value

This project demonstrates how data engineering practices can support customer churn analysis.

Potential business benefits include:

- Identifying customers who may be likely to leave.
- Understanding customer behavior and churn-related patterns.
- Supporting targeted customer retention strategies.
- Improving data quality for analytics and machine learning.
- Creating a reusable and maintainable data processing pipeline.

## Project Structure

The repository may be organized as follows, depending on the files included in the project:

```text
telecom-churn-prediction-medallion-architecture/
│
├── notebooks/
│   ├── bronze_layer
│   ├── silver_layer
│   └── gold_layer
│
├── data/
│   └── README.md
│
├── README.md
└── .gitignore
```

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Amit-khilar/Telecome_churn_prediction.git
   ```

2. Open the project in your Databricks workspace.

3. Configure the required catalog, schema, volume, and source file paths for your environment.

4. Run the notebooks in the correct sequence: Bronze → Silver → Gold.

5. Use the prepared Gold-layer data for churn analysis or the machine learning workflow implemented in the project.

**Note:** Execution requires an appropriately configured Databricks environment and access to the required source data.

## Expected Outcome

The project demonstrates an end-to-end, layered data processing approach for telecom churn analytics. It prepares structured, quality-checked data for downstream analysis and customer churn prediction.

Actual prediction performance and evaluation metrics should be added after running and evaluating the implemented machine learning model.

## Author

Developed as a hands-on data engineering and machine learning project to practice PySpark, Databricks, Delta Lake, and Medallion Architecture.

## Future Enhancements

- Build and evaluate churn classification models.
- Perform feature engineering and feature selection.
- Evaluate models using precision, recall, F1-score, and ROC-AUC.
- Create customer churn dashboards.
- Automate pipeline execution and monitoring.
- Develop targeted customer retention recommendations.

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 07:29:03 2025

@author: ngozi

Goal: Can the causal methods isolate the 3PL effect?
"""

import pandas as pd
from google.cloud import bigquery

# Define your GCP project and dataset
PROJECT_ID = "leadloom-466707"
DATASET_ID = "logistics_data"

# Initialize BigQuery client
client = bigquery.Client(project=PROJECT_ID)

# Mapping of table names to CSV file names
TABLES = {
    "customers": "customers.csv",
    "carrier_assignments": "carriers.csv",
    "shipments": "shipments.csv"
}

# Schema for each table (optional if autodetect works well)
# You can define custom schemas here if needed
# Otherwise, BigQuery can infer from CSV during load

def upload_csv_to_bigquery(table_name, file_path):
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,  # BigQuery tries to infer the schema
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  # Overwrite table
    )

    with open(file_path, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file, table_id, job_config=job_config
        )
    
    load_job.result()  # Wait for the job to complete
    print(f"✅ Loaded {file_path} into {table_id}")


if __name__ == "__main__":
    for table_name, csv_file in TABLES.items():
        try:
            upload_csv_to_bigquery(table_name, csv_file)
        except Exception as e:
            print(f"❌ Failed to load {csv_file} into {table_name}: {e}")




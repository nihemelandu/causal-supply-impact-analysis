# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 01:29:17 2025

@author: ngozi
"""

from google.cloud import bigquery

# Define project and dataset
PROJECT_ID = "leadloom-466707"
DATASET_ID = "logistics_data"

# Initialize BigQuery client
client = bigquery.Client(project=PROJECT_ID)

# 1. Create Dataset
def create_dataset():
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    dataset_ref.location = "US"
    
    try:
        client.create_dataset(dataset_ref, exists_ok=True)
        print(f"✅ Dataset '{DATASET_ID}' created or already exists.")
    except Exception as e:
        print(f"❌ Failed to create dataset: {e}")

# 2. Updated Table Schemas
SCHEMAS = {
    "customers": [
        bigquery.SchemaField("customer_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("customer_name", "STRING"),
        bigquery.SchemaField("customer_region", "STRING"),
        bigquery.SchemaField("customer_segment", "STRING"),
        bigquery.SchemaField("customer_quality_score", "FLOAT"),
        bigquery.SchemaField("signup_date", "DATE"),
    ],
    "carrier_assignments": [
        bigquery.SchemaField("carrier_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("carrier_name", "STRING"),
        bigquery.SchemaField("carrier_region", "STRING"),
        bigquery.SchemaField("is_3pl_partner", "BOOLEAN"),
        bigquery.SchemaField("service_level", "STRING"),
        bigquery.SchemaField("carrier_capability_score", "FLOAT"),
    ],
    "shipments": [
        bigquery.SchemaField("shipment_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("customer_id", "STRING"),
        bigquery.SchemaField("carrier_id", "STRING"),
        bigquery.SchemaField("shipment_date", "DATE"),
        bigquery.SchemaField("delivery_time_hours", "FLOAT"),
        bigquery.SchemaField("cost_usd", "FLOAT"),
        bigquery.SchemaField("delivered_on_time", "BOOLEAN"),
        bigquery.SchemaField("carrier_selection_method", "STRING"),
        bigquery.SchemaField("customer_satisfaction", "FLOAT"),
        bigquery.SchemaField("survey_date", "DATE"),
        bigquery.SchemaField("is_post_rollout", "BOOLEAN"),
        bigquery.SchemaField("is_algorithmic_selection", "BOOLEAN"),
    ]
}

# 3. Create Tables
def create_tables():
    for table_name, schema in SCHEMAS.items():
        table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"
        table = bigquery.Table(table_id, schema=schema)
        try:
            client.create_table(table, exists_ok=True)
            print(f"✅ Table '{table_name}' created or already exists.")
        except Exception as e:
            print(f"❌ Failed to create table '{table_name}': {e}")

# Run setup
if __name__ == "__main__":
    create_dataset()
    create_tables()

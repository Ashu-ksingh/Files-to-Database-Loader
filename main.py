import os
import pandas as pd
from sqlalchemy import create_engine
from etl.transform import transform_customers, transform_sales
from etl.load import create_table_if_not_exists, load_data
import json

# -----------------------------
# 1️ Database connection setup
# -----------------------------
db_config = {
    "user": "etl_user",
    "password": "ashu2909",
    "host": "localhost",
    "port": 5432,
    "database": "etl_demo",
    "dialect": "postgresql"
}

# SQLAlchemy engine
engine = create_engine(f"{db_config['dialect']}://{db_config['user']}:{db_config['password']}@"
                       f"{db_config['host']}:{db_config['port']}/{db_config['database']}")

# -----------------------------
# 2️ Extract: Load files
# -----------------------------
data_folder = "data"

# Customers JSON
customers_file = os.path.join(data_folder, "customers.json")
with open(customers_file, "r") as f:
    customers_df = pd.DataFrame(json.load(f))
print(f"Loaded {len(customers_df)} customers")

# Sales CSV
sales_file = os.path.join(data_folder, "sales_2023.csv")
sales_df = pd.read_csv(sales_file)
print(f"Loaded {len(sales_df)} sales records")

# -----------------------------
# 3️ Transform
# -----------------------------
customers_transformed = transform_customers(customers_df)
sales_transformed = transform_sales(sales_df)
print("Data transformed successfully!")

# -----------------------------
# 4️ Load
# -----------------------------
# Create tables if not exists
create_table_if_not_exists(engine, "customers", customers_transformed)
create_table_if_not_exists(engine, "sales", sales_transformed)

# Load data into tables
load_data(engine, "customers", customers_transformed)
load_data(engine, "sales", sales_transformed)

print("ETL process completed successfully!")

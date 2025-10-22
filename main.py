# main.py
import os
import logging
from etl.extract import read_csv, read_json
from etl.transform import transform_customers, transform_sales
from etl.load import create_table_if_not_exists, load_data
from sqlalchemy import create_engine
import json

# ---------- Setup Logging ----------
logging.basicConfig(
    filename='etl_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------- Load DB Config ----------
with open("config/db_config.json") as f:
    db_config = json.load(f)

DB_URL = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(DB_URL)

# ---------- File Paths ----------
DATA_DIR = "data"
CUSTOMER_FILE = os.path.join(DATA_DIR, "customers.json")
SALES_FILE = os.path.join(DATA_DIR, "sales_2023.csv")

def run_etl():
    try:
        logging.info("ETL process started.")

        # ---------- Extract ----------
        logging.info(f"Reading file: {CUSTOMER_FILE}")
        customers = read_json(CUSTOMER_FILE)
        
        logging.info(f"Reading file: {SALES_FILE}")
        sales = read_csv(SALES_FILE)

        # ---------- Transform ----------
        logging.info("Transforming customer data")
        customers_transformed = transform_customers(customers)
        
        logging.info("Transforming sales data")
        sales_transformed = transform_sales(sales)

        # ---------- Load ----------
        logging.info("Creating and loading tables")
        create_table_if_not_exists(engine, 'customers', customers_transformed)
        load_data(engine, 'customers', customers_transformed)

        create_table_if_not_exists(engine, 'sales', sales_transformed)
        load_data(engine, 'sales', sales_transformed)

        logging.info("ETL process completed successfully.")
        print("ETL completed successfully!")

    except Exception as e:
        logging.error(f"ETL failed: {e}")
        print(f"ETL failed: {e}")

if __name__ == "__main__":
    run_etl()

# Files-to-Database Loader (Python + PostgreSQL)

A simple **ETL pipeline** that reads CSV and JSON files, transforms the data, and loads it into PostgreSQL. Designed to showcase **Python, Pandas, SQL, and ETL skills** for data engineering roles.

---

## Tech Stack
- **Python 3**
- **Pandas** for data processing
- **SQLAlchemy + PostgreSQL** for database operations
- Logging for ETL monitoring

---

## Features
- Reads multiple CSV/JSON files
- Cleans and transforms data
- Automatically creates tables if not exist
- Loads data into PostgreSQL
- Logging and exception handling

---

## Project Structure

files_to_db_loader/
├── config/db_config.json
├── data/customers.json
├── data/sales_2023.csv
├── etl/extract.py
├── etl/transform.py
├── etl/load.py
├── main.py
└── README.md


## Run Instructions
1. Install dependencies:

	--pip install pandas sqlalchemy psycopg2
	Configure PostgreSQL (db_config.json) with your credentials.

2. Place your CSV/JSON files in the data/ folder.

3. Run ETL:

	python main.py
	Check tables and logs in PostgreSQL / etl_log.log.


Author:
Ashutosh Kumar Singh – Aspiring Data Engineer
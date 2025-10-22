# Files-to-Database-Loader (Python + PostgreSQL)
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL. It extracts data from CSV and JSON files, performs transformations, and loads the cleaned data into a PostgreSQL database.

This project is designed for resume and portfolio purposes, showcasing practical data engineering skills including data cleaning, transformation, and database operations.

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

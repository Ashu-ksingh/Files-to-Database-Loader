from sqlalchemy import text, inspect

def create_table_if_not_exists(engine, table_name, df_sample):
    """
    Create table if it does not exist.
    Uses Pandas to_sql for simplicity.
    Checks if table already exists using SQLAlchemy inspector.
    """
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        df_sample.head(0).to_sql(table_name, engine, if_exists='fail', index=False)
        print(f"Table '{table_name}' created successfully.")
    else:
        print(f"Table '{table_name}' already exists.")

def load_data(engine, table_name, df):
    """
    Load DataFrame into the database table.
    Appends data if table exists.
    """
    try:
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data loaded into table '{table_name}' successfully.")
    except Exception as e:
        print(f"Failed to load data into table '{table_name}': {e}")

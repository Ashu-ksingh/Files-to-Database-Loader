import pandas as pd

def transform_customers(df):
    """
    Transform customer data:
    - Strip whitespace
    - Capitalize names properly
    - Ensure emails are lowercase
    - Convert joined date to datetime
    """
    df['name'] = df['name'].str.strip().str.title()
    df['email'] = df['email'].str.strip().str.lower()
    df['joined'] = pd.to_datetime(df['joined'])
    return df

def transform_sales(df):
    """
    Transform sales data:
    - Convert order_date to datetime
    - Ensure product names are title case
    - Amount remains float
    """
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['product'] = df['product'].str.strip().str.title()
    df['amount'] = df['amount'].astype(float)
    return df

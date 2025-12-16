import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def load_orders_data(df: pd.DataFrame, db_url: str, table_name: str = "orders" ):
    """
    Loads order data into a PostgreSQL database.

    Parameters:
    df : pd.DataFrame
        The DataFrame containing order data to be loaded.
    table_name : str
        The name of the target table in the database.
    db_url : str
        The database connection URL.
    """
    try:
        engine = create_engine(db_url)
        
        #tulis ke tabel
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"[LOAD]Order data berhasil dibuat'{table_name}'.")

    except SQLAlchemyError as e:
        print(f"[LOAD]Error saat memuat data order ke database: str{e}")




from config.db_config import DB_URL

#ETL airtimes
from src.etl_airtimes.extract import extract_airtime_data
from src.etl_airtimes.transform import transform_airtime_data
from src.etl_airtimes.load import load_airtime_data

#ETL orders
from src.etl_orders.extract import extract_orders_data
from src.etl_orders.transform import transform_orders_data
from src.etl_orders.load import load_orders_data

#ETL surveys
from src.etl_surveys.extract import extract_surveys_data 
from src.etl_surveys.transform import transform_survey_data
from src.etl_surveys.load import load_survey_data


# ============================== AIRTIME Pipelines ==============================
def run_airtime_etl(file_path: str):
    print("[AIRTIME ETL] Starting ETL process for airtime data...")

    df = extract_airtime_data(file_path)
    print(f"[AIRTIME ETL] Extracted {len(df)} rows.")
    
    df = transform_airtime_data(df)
    print(f"[AIRTIME ETL] Transformed data to {len(df)} rows.")

    load_airtime_data(df, DB_URL)
    print(f"[AIRTIME ETL] Loaded data into the database.")


# ============================== ORDERS Pipelines ==============================
def run_orders_etl(file_path: str):
    print(f"[ORDERS ETL] Starting ETL process for orders data...")

    df = extract_orders_data(file_path)
    print(f"[ORDERS ETL] Extracted {len(df)} rows.")
    
    df = transform_orders_data(df)
    print(f"[ORDERS ETL] Transformed data to {len(df)} rows.")

    load_orders_data(df, DB_URL)
    print(f"[ORDERS ETL] Loaded data into the database.")


# ============================== SURVEYS Pipelines ==============================
def run_surveys_etl(file_path: str):
    print(f"[SURVEYS ETL] Starting ETL process for surveys data...")

    df = extract_surveys_data(file_path)
    print(f"[SURVEYS ETL] Extracted {len(df)} rows.")
    
    df = transform_survey_data(df)
    print(f"[SURVEYS ETL] Transformed data to {len(df)} rows.")

    load_survey_data(df,DB_URL)
    print(f"[SURVEYS ETL] Loaded data into the database.")

# ============================== RUN SEMUA ==============================
def run_all_etl(file_path: str):
    run_airtime_etl(file_path)
    run_orders_etl(file_path)
    run_surveys_etl(file_path)
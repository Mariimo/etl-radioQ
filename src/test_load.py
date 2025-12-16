from src.etl_airtimes.extract import extract_airtime_data
from src.etl_airtimes.transform import transform_airtime_data
from src.etl_airtimes.load import load_airtime_data
from config.db_config import DB_URL

file_path = "data/raw/Data_Radio_q.xlsx"
sheet_name = "JAM TAYANG 2018"

df = extract_airtime_data(file_path, sheet_name)
df = transform_airtime_data(df)

load_airtime_data(df, DB_URL)
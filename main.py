from src.orchestrator import (
    run_airtime_etl,
    run_orders_etl,
    run_surveys_etl
)

if __name__ == "__main__":
    FILE_PATH = "data/raw/Data_Radio_q.xlsx"

    print("===== RADIO Q ETL (DEBUG MODE) =====")

    # Pilih ETL yang mau dijalankan:
    # run_airtime_etl(FILE_PATH)
    # run_orders_etl(FILE_PATH)
    # run_surveys_etl(FILE_PATH)

    # Untuk run semua:
    run_airtime_etl(FILE_PATH)
    run_orders_etl(FILE_PATH)
    run_surveys_etl(FILE_PATH)

    print("===== DONE =====")

# ETL RadioQ Data Pipeline

End-to-end ETL (Extract, Transform, Load) pipeline project for RadioQ data, built as a Data Engineering portfolio project.  
This pipeline processes multiple Excel-based datasets and loads clean, structured data into a PostgreSQL database (Supabase).

---

## 📌 Overview

This project implements a modular ETL architecture to handle RadioQ operational data, including:

- **Airtime data** (jam tayang siaran)
- **Advertising orders data**
- **Listener survey data**

Each dataset is processed through a dedicated ETL pipeline and orchestrated centrally for maintainability and scalability.

---

## 🛠 Tech Stack

- **Language**: Python
- **Data Processing**: Pandas
- **Database**: PostgreSQL (Supabase)
- **Architecture**: Modular ETL + Orchestrator Pattern
- **Version Control**: Git & GitHub

---

## 📂 Data Sources

All data sources are stored as Excel files:

- `Data_Radio_q.xlsx`
  - Airtime sheets (e.g. `JAM TAYANG 2018`)
  - Orders sheets (e.g. `ORDER IKLAN 2020`)
  - Survey sheets (e.g. `DATA RESPON PENDENGAR 2022`)

Sheet selection is handled dynamically using **regex-based extraction**.

---

## 🏗 ETL Architecture

┌──────────────┐
│ Excel Files │
└──────┬───────┘
│
▼
┌───────────────────┐
│ Extract Layer │
│ (Regex-based) │
└──────┬────────────┘
│
▼
┌───────────────────┐
│ Transform Layer │
│ - Cleaning │
│ - Normalization │
│ - Deduplication │
└──────┬────────────┘
│
▼
┌───────────────────┐
│ Load Layer │
│ PostgreSQL │
│ (Supabase) │
└───────────────────┘
## 📁 Project Structure

radioq_etl_big/
├── config/
│ └── db_config.py
├── data/
│ ├── raw/
│ └── processed/
├── src/
│ ├── etl_airtimes/
│ │ ├── extract.py
│ │ ├── transform.py
│ │ └── load.py
│ ├── etl_orders/
│ │ ├── extract.py
│ │ ├── transform.py
│ │ └── load.py
│ ├── etl_surveys/
│ │ ├── extract.py
│ │ ├── transform.py
│ │ └── load.py
│ └── orchestrator.py
├── main.py
└── README.md

yaml
Copy code

---

## ⚙️ How to Run

### 1. Clone Repository
```bash
git clone https://github.com/Mariimo/etl-radioQ.git
cd etl-radioQ

2. Install Dependencies
pip install pandas sqlalchemy psycopg2

3. Configure Database

Update database connection in:

config/db_config.py

DB_URL = "postgresql://user:password@host:port/database"

4. Run ETL Pipeline
python main.py

🚀 Pipeline Execution

By default, main.py runs:

Airtime ETL

Orders ETL

Surveys ETL

Each pipeline logs:

Extracted rows

Transformed rows

Load status

🗄 Database Tables

The pipeline creates and loads data into:

airtimes

orders

surveys

All tables are stored in PostgreSQL (Supabase).

✅ Key Features

Regex-based dynamic sheet extraction

Modular ETL design

Centralized orchestration

Production-ready project structure

Suitable for Data Engineer portfolio

📈 Future Improvements

Add logging & monitoring

Schedule with Apache Airflow

Add data quality checks

Implement incremental loading

👤 Author

Mariimo
Data Engineer Portfolio Project
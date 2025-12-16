from etl_airtimes.extract import extract_airtime_data

file_path = r"D:\Fathi melondre\Data Engineer\Portofolio\radioq_etl_big\data\raw\Data_Radio_q.xlsx"
sheet_name = "JAM TAYANG 2018"

df = extract_airtime_data(file_path, sheet_name)

print(" \n=== HEAD ===")
print(df.head())

print(" \n=== CLOUMNS ===")
print(df.columns)

print(" \n=== BODY ===")
print(df)

print(" \n=== TOTAL ENTRY ===")
print(len(df))

print(" \n=== INFO ===")
print(df.info())



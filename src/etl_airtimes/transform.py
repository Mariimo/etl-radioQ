import pandas as pd

def betulin_jam_tayang_mulai(value):
    if pd.isna(value):
        return None
    text = str(value)
    if "-" not in text:
        return text.strip()   # tidak ada tanda "-", return apa adanya
    return text.split("-")[0].strip()


def betulin_jam_tayang_selesai(value):
    if pd.isna(value):
        return None
    text = str(value)
    if "-" not in text:
        return None           # kalau tidak ada jam selesai, anggap None
    parts = text.split("-")
    if len(parts) < 2:
        return None
    return parts[1].strip()


def normalisasi_hari_tayang(value):
    value = str(value).strip().lower()

    #mapping hari
    days = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]

    if value == "SETIAP HARI" :
        return days
    
    #hari nya ada tanda hubung -
    if "-" in value:
        start, end = [v.strip().upper() for v in value.split("-")]
        return [start, end]
    
    #hari biasa
    return [value]

def ambil_tahun(value):
    #ambil 4 angka terakhir
    import re
    match = re.search(r'(\d{4})$', str(value))
    return int(match.group(1)) if match else None




def transform_airtime_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the airtime data by cleaning and formatting.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the airtime data.

    Returns:
    pd.DataFrame: A DataFrame containing the transformed airtime data.
    """
    

    # Example transformation: Remove duplicates and fill missing values
    df = df.drop_duplicates(subset=["Nama Program","Hari Tayang", "Jam Tayang Mulai", "Jam Tayang Selesai", "Tahun"])
    
    # Additional transformations can be added here
    
    #hari tayang di normalisasikan
    df["Hari Tayang"] = df["Hari Tayang"].apply(normalisasi_hari_tayang)
    df = df.explode("Hari Tayang")

    #betulin jam tayang mulai dan selesai
    df["Jam Tayang Mulai"] = df["Jam Tayang Mulai"].apply(betulin_jam_tayang_mulai)
    
    
    df["Jam Tayang Selesai"] = df["Jam Tayang Selesai"].apply(betulin_jam_tayang_selesai)
   

    #Kolom tahun
    df["Tahun"] = df["Tahun"].apply(ambil_tahun)

   


    return df
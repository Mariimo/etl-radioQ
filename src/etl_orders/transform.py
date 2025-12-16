import pandas as pd

def betulin_value_durasi(value):
    if pd.isna(value):
        return None
    
    val = str(value).lower()

    val = val.replace(" ","")
    val = val.replace("--","-").replace("–","-").replace("—","-")

    #ubah 30-60 detik jadi 45 detik
    if ("30-60") in val:
        return "45 Detik"
    
    return value
    
    


def transform_orders_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the order data by cleaning and formatting.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the order data.

    Returns:
    pd.DataFrame: A DataFrame containing the transformed order data.
    """
    print("\n[DEBUG] Columns in Orders DF:", df.columns.tolist())

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    subset_cols = [
    "nama_pengiklan",
    "kategori_brand",
    "spots",
    "durasi_iklan",
    "jenis_iklan",
    "tarif_iklan",
    "tahun"
]

    df = df.drop_duplicates(subset=subset_cols, ignore_index=True)
    
    # Additional transformations can be added here
    
    #betulin durasi iklan dan value durasi
    
    df["durasi_iklan"] = df["durasi_iklan"].apply(betulin_value_durasi)
    

    #Kolom tahun
    df["tahun"] = df["tahun"].astype(int)

    return df
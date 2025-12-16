import pandas as pd


def transform_survey_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the survey data by cleaning and formatting.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the survey data.

    Returns:
    pd.DataFrame: A DataFrame containing the transformed survey data.
    """
    
     # 1. Drop unnecessary columns
    
    columns_to_drop = ['No']  # Replace with actual column names
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
   

    if "Nama Depan" in df.columns and "Nama Belakang" in df.columns:
        df["nama"] = df["Nama Depan"].astype(str).str.strip() + " " + df["Nama Belakang"].astype(str).str.strip()

    elif "Nama Depan" in df.columns:
        df["Nama"] = df["Nama Depan"].astype(str).str.strip()

    df = df.drop(columns=[col for col in ["Nama Depan", "Nama Belakang"] if col in df.columns])




    rename_map = {
        "NAMA DEPAN": "nama",
        "Nama Depan": "nama",
        "Nama Belakang": "nama",
        "Umur": "umur",
        "Jenis Kelamin": "jenis_kelamin",
        "Pekerjaan": "pekerjaan",
        "Asal": "asal",
        "Program Favorit": "program_favorit",
        "Bulan": "bulan_survey",
    }

    df = df.rename(columns={k: v for k, v in rename_map.items() if v is not None})


    # 2. Clean names (remove titles, trim spaces, proper case)
    
    def clean_name(name):
        if pd.isna(name):
            return None
        # Remove common titles
        titles = ["Dr", "Ir", "H", "S.H", "M.Pd", "A.Md", "M.Kom", "dkk", "Dra", "Dr .", "dr .","Ir . ","Dr.","dr.","Ir.","Dr. ","Ir. ", ".",","]
        for t in titles:
            name = name.replace(t, '')
        # Trim spaces and convert to proper case
        name = ' '.join(name.split()).title()
        return name.title()
    
    if "nama" in df.columns:
        df["nama"] = df["nama"].apply(clean_name)


    # 3. Normalize gender values
    
    def normalize_gender(x):
        x= str(x).strip().lower()
        if x in ["pria", "laki-laki", "cowok", "lelaki", "Jantan","Pria"]:
            return "Laki-laki"
        elif x in ["wanita", "perempuan", "cewek","betina","Wanita"]:
            return "Perempuan"
        else:
            return None

    if "jenis_kelamin" in df.columns:
        df["jenis_kelamin"] = df["jenis_kelamin"].apply(normalize_gender)



    # 4. Normalize city column
    
    if "asal" in df.columns:
        df["asal"] = df["asal"].astype(str).str.strip().str.title()


    # 5. Convert age to integer
    
    if "umur" in df.columns:
        df["umur"] = pd.to_numeric(df["umur"], errors="coerce").astype("Int64")

    # 6. Create age_group column
    def age_group(age):
        if pd.isna(age):
            return None
        if age < 18:
            return "Anak - anak"
        elif age <= 30:
            return "Dewasa Muda"
        elif age <= 50:
            return "Dewasa"
        else:
            return "Lansia"
            
    df["age_group"] = df["umur"].apply(age_group)

    # 9. Rename columns to snake_case
    df.columns = df.columns.str.lower().str.replace(" ", "_")


    return df
import pandas as pd
import os
import re

def extract_airtime_data(file_path: str) -> pd.DataFrame:
    """
    Extracts airtime data from a excel file.

    Parameters:
    file_path : The path to the excel file containing airtime data.

    Returns:
    pd.DataFrame: A DataFrame containing the extracted airtime data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    xls = pd.ExcelFile(file_path)
    all_sheet = xls.sheet_names

    pattern = r"JAM TAYANG\s*(\d{4})"
    df_list=[]

    for sheet in all_sheet:
        match= re.search(pattern, sheet.upper())

        if match:
            tahun = match.group(1)

            df = pd.read_excel(file_path, sheet_name=sheet)
            df["Tahun"] = tahun

            df_list.append(df)

    if not df_list:
        raise ValueError("No matching sheets found in the Excel file.")
    
    airtime_data = pd.concat(df_list, ignore_index=True)
    return airtime_data
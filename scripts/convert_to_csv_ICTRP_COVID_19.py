from pathlib import Path
import sys
import pandas as pd
import xlrd
import csv

DOWNLOAD_DIR = 'download'
PROCESSED_DIR = 'data'

def clean_csv(origin_file_path, processed_file_path):
    df = pd.read_csv(origin_file_path)
    date_cols = ['Last Refreshed on', 'Date registration',
                'Date enrollement', 'results date posted',
                'results date completed']
    datetime_cols = ['Export date']
    datestr_cols = ['Date registration3']

    for col in date_cols + datetime_cols:
        df[col] = pd.to_datetime(df[col])

    for col in datestr_cols:
        df[col] = pd.to_datetime(df[col], format = "%Y%m%d")

    df.to_csv(processed_file_path, index=False, quoting=csv.QUOTE_ALL)

if __name__ == "__main__":
    file_name_csv_origin = 'ICTRP_COVID_19.csv'
    file_name_csv_processed = 'ICTRP_COVID_19.csv'
    download_path = Path(DOWNLOAD_DIR)
    processed_path = Path(PROCESSED_DIR)
    processed_path.mkdir(parents=True, exist_ok=True)

    clean_csv(download_path.joinpath(file_name_csv_origin), processed_path.joinpath(file_name_csv_processed))

from pathlib import Path
import sys
import pandas as pd
import xlrd
import csv

DOWNLOAD_DIR = 'download'
PROCESSED_DIR = 'data'

def xls_to_csv_(xls_file_path, csv_file_path):
    with open(xls_file_path, mode='rb') as xls_file_handler:
        data_xls = pd.read_excel(xls_file_handler, index_col=None)
        data_xls.to_csv(csv_file_path, encoding='utf-8')

def xls_to_csv(xls_file_path, csv_file_path):
    wb = xlrd.open_workbook(xls_file_path, encoding_override='utf-8', formatting_info=True)
    sh = wb.sheet_by_index(0)
    your_csv_file = open(csv_file_path, 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    header = sh.row_values(0)
    date_cols = ['Last Refreshed on', 'Date registration',
                'Date enrollement', 'results date posted',
                'results date completed']
    datetime_cols = ['Export date']
    datestr_cols = ['Date registration3']

    date_cols_indices = {header.index(col) for col in date_cols}
    datetime_cols_indices = {header.index(col) for col in datetime_cols}
    datestr_cols_indices = {header.index(col) for col in datestr_cols}
    
    for rowIdx in range(sh.nrows):
        row_values = sh.row_values(rowIdx)
        header_idx = 0
        if rowIdx != header_idx:
            for colIdx in range(len(row_values)):
                cell_value = row_values[colIdx]
                if cell_value != '':
                    if colIdx in date_cols_indices:
                        year, month, day, _, _, _ = xlrd.xldate_as_tuple(cell_value, wb.datemode)
                        row_values[colIdx] = "%04d-%02d-%02d" % (year, month, day)
                    elif colIdx in datetime_cols_indices:
                        year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(cell_value, wb.datemode)
                        row_values[colIdx] = "%04d-%02d-%02d %02d:%02d:%02d " % (year, month, day, hour, minute, sec)
                    elif colIdx in datestr_cols_indices:
                        cell_value = str(int(cell_value))
                        year, month, day = int(cell_value[:4]), int(cell_value[4:6]), int(cell_value[6:])
                        row_values[colIdx] = "%04d-%02d-%02d" % (year, month, day)
        wr.writerow(row_values)

    your_csv_file.close()

if __name__ == "__main__":
    file_name_xls = 'ICTRP_COVID_19.xls'
    file_name_csv = 'ICTRP_COVID_19.csv'
    download_path = Path(DOWNLOAD_DIR)
    processed_path = Path(PROCESSED_DIR)
    processed_path.mkdir(parents=True, exist_ok=True)

    xls_to_csv(download_path.joinpath(file_name_xls), processed_path.joinpath(file_name_csv))
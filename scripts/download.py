import urllib.request
from pathlib import Path
import zipfile
import socket

TIMEOUT = 5 # WHO server is too busy ...
DOWNLOAD_DIR = 'download'

static_content_URLs = {
    "ICTRP_Weekly_2_March_2020_CSV.zip" : "https://www.who.int/ictrp/ICTRPWeek2March2020.zip",
    "ICTRP_Weekly_9_March_2020_CSV.zip" : "https://www.who.int/ictrp/ICTRPWeek9March2020.zip",
    "ICTRP_Weekly_16_March_2020_CSV.zip" : "https://www.who.int/ictrp/ICTRPWeek16March2020.zip",
    "ICTRP_Weekly_23_March_2020_CSV.zip" : "https://www.who.int/ictrp/ICTRPWeek23March2020.zip",
    "ICTRP_Weekly_30_March_2020_CSV.zip" : "https://www.who.int/ictrp/ICTRPWeek30March2020.zip"
}

dynamic_content_URLs = {
    "ICTRP_COVID_19.xls" : "https://www.who.int/docs/default-source/coronaviruse/covid-19-trials.xls",
    "ClinicalTrials.gov_COVID_19.csv" : "https://www.clinicaltrials.gov/ct2/results/download_fields?down_count=10000&down_flds=all&down_fmt=csv&cond=COVID-19&flds=a&flds=b&flds=y",
    "ClinicalTrials.gov_COVID_19_full_xml.zip" : "https://www.clinicaltrials.gov/ct2/results/download_studies?cond=COVID-19"
}

def download_unzip(name, url, download_path, force_download = False):
    try :
        file_path = download_path.joinpath(name)
        if not file_path.exists() or force_download:
            request = urllib.request.urlopen(url, timeout=TIMEOUT)
            with open(file_path, 'wb') as file_handler:
                file_handler.write(request.read())
            if name[-4:] == '.zip':
                zip_dir_path = download_path.joinpath(name[:-4])
                with zipfile.ZipFile(file_path, "r") as zip_ref:
                    zip_ref.extractall(zip_dir_path)
    except Exception as e: 
        print(url, e)

if __name__ == "__main__":
    download_path = Path(DOWNLOAD_DIR)
    download_path.mkdir(parents=True, exist_ok=True)

    for name, url in static_content_URLs.items():
        print('Downloading ' + name + ' ...')
        download_unzip(name, url, download_path)
            
    for name, url in dynamic_content_URLs.items():
        print('Downloading ' + name + ' ...')
        download_unzip(name, url, download_path, force_download=True)


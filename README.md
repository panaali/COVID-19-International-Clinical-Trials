# COVID-19-International-Clinical-Trials
COVID-19 International Clinical Trials


# Requirements
- Python 3

# Installation
```bash
pip install xlrd
pip install xmltodict
```
# Usage
```bash
python scripts/download.py
python scripts/convert_to_csv_ICTRP_COVID_19.py
python scripts/convert_to_csv_ClinicalTrials.gov_COVID_19_full_xml.py
cp download/ClinicalTrials.gov_COVID_19.csv data/ClinicalTrials.gov_COVID_19.csv
mkdir data/ICTRP_weekly
cp download/ICTRP*/*.csv data/ICTRP_weekly/
```
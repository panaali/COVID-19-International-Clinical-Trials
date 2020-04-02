from pathlib import Path
import xmltodict, json

DOWNLOAD_DIR = 'download'
PROCESSED_DIR = 'data'

def xml_to_csv(xml_file_path, json_file_path):
    with open(xml_file_path) as xml_file_handler:
        o = xmltodict.parse(xml_file_handler.read())
        with open(json_file_path, "w") as json_file:
            json_file.write(json.dumps(o))

if __name__ == "__main__":
    dir_name_xml = 'ClinicalTrials.gov_COVID_19_full_xml'
    dir_name_json = 'ClinicalTrials.gov_COVID_19_full_json'
    download_path = Path(DOWNLOAD_DIR)
    processed_path = Path(PROCESSED_DIR)
    json_dir_path = processed_path.joinpath(dir_name_json)
    xml_dir_path = download_path.joinpath(dir_name_xml)

    processed_path.mkdir(parents=True, exist_ok=True)
    json_dir_path.mkdir(parents=True, exist_ok=True)

    for file_path in xml_dir_path.iterdir():
        if file_path.is_file() and file_path.suffix == '.xml':
            file_name_json = file_path.stem + '.json'
            xml_to_csv(file_path, json_dir_path.joinpath(file_name_json))
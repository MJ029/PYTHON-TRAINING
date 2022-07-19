import pandas as pd
import os


def create_non_existing_dir(dir_path: str):
    abs_path = os.path.abspath(dir_path)
    if os.path.isdir(dir_path):
        print("Path Exists...! Continue...")
    else:
        print("Path Does Not Exists...! Creating the Directory.")
        os.makedirs(abs_path)
        return abs_path


# convert Excel to JSON file
file_path = "../../dataset/File-Handling/Excel-Reading/Data-Generation.xlsx"

target_path = "../../dataset/output"

file_name = "Claims-History"

df = pd.read_excel(file_path, sheet_name='CLAIMS-HISTORY')

target_file_path = "/".join([target_path, "EXCEL-JSON", file_name])

target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

complete_file_path = "/".join([target_file_abs_path, f"{file_name}.json"])

df.to_json(complete_file_path)

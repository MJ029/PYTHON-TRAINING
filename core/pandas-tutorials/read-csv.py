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


# convert csv to Excel file
file_path = "../../dataset/File-Handling/CSV-Reading/Claims-History/Claims-History.csv"

target_path = "../../dataset/output"

file_name = "Claims-History"

excel_filename = "Claims-History.xlsx"

if __name__ == "__main__":
    df = pd.read_csv(file_path)

    target_file_path = "/".join([target_path, "CSV-EXCEL", file_name])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_file_path = "/".join([target_file_abs_path, f"{file_name}.xlsx"])

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

    os.makedirs(abs_path)
    return abs_path


# convert excel to parquet file
file_path = "../../dataset/File-Handling/Excel-Reading/Data-Generation.xlsx"

target_path = "../../dataset/output"

file_name = "Claims-History"

if __name__ == "__main__":

    df = pd.read_excel(file_path, sheet_name="CLAIMS-HISTORY")

    target_file_path = "/".join([target_path, "EXCEL-PARQUET"])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_path = "/".join([target_file_abs_path, f"{file_name}.parquet"])

    df.to_parquet(complete_path)

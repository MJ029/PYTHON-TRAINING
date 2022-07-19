import pandas as pd
import os


def create_non_existing_dir(dir_path: str):
    abs_path = os.path.abspath(dir_path)
    os.makedirs(abs_path)
    return abs_path


# convert csv to parquet file
file_path = "../../dataset/File-Handling/CSV-Reading/Claims-History/Claims-History.csv"

target_path = "../../dataset/output"

file_name = "Claims-History"

if __name__ == "__main__":

    df = pd.read_csv(file_path)

    target_file_path = "/".join([target_path, "CSV-PARQUET"])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_file_path = "/".join([target_file_abs_path, f"{file_name}.parquet"])

    df.to_parquet(complete_file_path, index=False)

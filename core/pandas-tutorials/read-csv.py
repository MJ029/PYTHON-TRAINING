import os
import pandas as pd


def create_non_existing_dir(dir_path: str):
    abs_path = os.path.abspath(dir_path)
    try:
        if os.path.isdir(dir_path):
            print("Path Exists...! Continue...")
        else:
            print("Path Does Not Exists...! Creating the Directory.")
            os.makedirs(abs_path)
        return abs_path
    except Exception as e:
        raise e


if __name__ == "__main__":

    # # declare Constants
    # file_path = "../../dataset/File-Handling/CSV-Reading/Claims-Master/Claims-Master.csv"
    #
    # # Read Data Frame
    # claims_master_df = pd.read_csv(file_path)
    # claims_master_df_cleansed = claims_master_df.dropna()
    # print(claims_master_df)
    # print(claims_master_df_cleansed)

    # File Reading Automation
    file_path = "../../dataset/File-Handling/CSV-Reading"
    targe_path = "../../dataset/output"
    file_names = ["Claims-History", "Claims-Master"]
    for file_name in file_names:
        try:
            print(f"Running File: {file_name}")
            # Path Generation (or) Modification
            complete_path = "/".join([file_path, file_name, f"{file_name}.csv"])

            # Read Object as DataFrame
            df = pd.read_csv(complete_path)
            df = df.dropna()

            # Write Output to Target Path
            target_file_path = "/".join([targe_path, "CSV-Writing", file_name])
            target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)
            print(target_file_abs_path)

            complete_file_path = "/".join([target_file_abs_path, f"{file_name}.csv"])
            df.to_csv(complete_file_path, index=False)
        except Exception as e:
            print(e)
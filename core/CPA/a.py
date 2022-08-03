import mysql.connector as ctr
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


target_path = "../../core/CPA"
file_name = "sample"

if __name__ == "__main__":

    mydb = ctr.connect(host="localhost", database="sql_learning", user="root", password="blackforest")

    query = "Select * from table_j;"

    df = pd.read_sql(query, con=mydb)

    target_file_path = "/".join([target_path, file_name])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_file_path = "/".join([target_file_abs_path, f"{file_name}.csv"])

    df.to_csv(complete_file_path, index=False)

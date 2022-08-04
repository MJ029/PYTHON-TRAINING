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


file_name = "18"
target_path = "../../PANDAS_SQL"


if __name__ == "__main__":

    connection = ctr.connect(user='root', host='localhost', password='blackforest', database='sql_learning')

    query =  "SELECT * FROM ( SELECT RANK() OVER( ORDER BY NumDealsPurchases DESC, Income DESC ) AS TOP_3_customers, ID, Income, NumDealsPurchases FROM customer_campaign ) AS tmp WHERE tmp.TOP_3_customers <= 3;"

    df = pd.read_sql(sql=query,con=connection)

    target_file_path = "/".join([target_path, file_name])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_file_path = "/".join([target_file_abs_path, f"{file_name}.csv"])

    df.to_csv(complete_file_path, index=False)



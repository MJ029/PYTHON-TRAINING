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


file_name = "21"
target_path = "../../PANDAS_SQL"


if __name__ == "__main__":

    connection = ctr.connect(user='root', host='localhost', password='blackforest', database='sql_learning')

    query = """SELECT category, COUNT(ID) AS customers 
    FROM (SELECT CASE WHEN Income < (SELECT AVG(Income) FROM customer_campaign) 
    THEN "BELOW_AVERAGE" WHEN Income >= (SELECT AVG(Income) FROM customer_campaign)
    THEN "ABOVE_AVERAGE" ELSE "NOT_FOUND" END AS category, ID FROM customer_campaign )
    AS tmp GROUP BY category ORDER BY category;"""

    df = pd.read_sql(sql=query,con=connection)

    target_file_path = "/".join([target_path, file_name])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_file_path = "/".join([target_file_abs_path, f"{file_name}.csv"])

    df.to_csv(complete_file_path, index=False)



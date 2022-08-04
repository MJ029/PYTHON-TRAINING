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


file_name = "customer_campaign"
target_path = "../../PANDAS_SQL"


if __name__ == "__main__":

    connection = ctr.connect(user='root', host='localhost', password='blackforest', database='sql_learning')

    Table = {}

    """CREATE TABLE IF NOT EXISTS 'customer_campaign'
    SELECT c.ID,
    c.KidHome
    SELECT c.ID,
    STR_TO_DATE(c.Dt_customer, '%d-%m-%Y') AS join_date,
    STR_TO_DATE (CONCAT(c.Year_Birth, '-01-01'), '%Y-%m-%d') AS YOB,
    TRIM(c.Education) AS education,
    TRIM(c.Marital_Status) AS martial_status,
    CAST(c.Income AS DECIMAL(28, 2)) AS Income
    ,c.Teenhome
    ,c.Recency
    ,c.Complain
    ,p.NumWebPurchases
    ,p.NumCatalogPurchases
    ,p.NumStorePurchases
    ,p.NumWebVisitsMonth
    ,q.MntWines
    ,q.MntFruits
    ,q.MntMeatProducts
    ,q.MntFishProducts
    ,q.MntSweetProducts
    ,q.MntGoldProds
    ,r.NumDealsPurchases
    ,r.AcceptedCmp1
    ,r.AcceptedCmp2
    ,r.AcceptedCmp2
    ,r.AcceptedCmp3
    ,r.AcceptedCmp4
    ,r.AcceptedCmp5
    ,r.Response
    FROM customer_details AS c
    JOIN places_details AS p ON c.ID = p.ID
    JOIN product_details AS q ON c.ID = q.ID
    JOIN promotions_details AS r ON c.ID = r.ID;"""

    table_name = "customer_campaign"

    query = f"SELECT * FROM {table_name}"

    df = pd.read_sql(sql=query, con=connection)

    # df = pd.read_sql_table(table_name='customer_campaign', con=connection)
    target_file_path = "/".join([target_path, file_name])

    target_file_abs_path = create_non_existing_dir(dir_path=target_file_path)

    complete_file_path = "/".join([target_file_abs_path, f"{file_name}.csv"])

    df.to_csv(complete_file_path, index=False)


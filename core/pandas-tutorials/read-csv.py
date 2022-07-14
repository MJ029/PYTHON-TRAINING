import pandas as pd

#Reading multiple CSV file

file_path = "../../dataset/File-Handling/CSV-Reading"
file_names = ["Claims-History", "Claims-Master", "Employee-Master", "Salary-History"]

for file_name in file_names:

    print(f"Running File: {file_name}")

    df = pd.read_csv(file_path + f"/{file_name}" + f"/{file_name}.csv")
    df.to_parquet

    print(df)

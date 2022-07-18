import pandas as pd


# Filter NA records and write as CSV file

file_path = "../../dataset/File-Handling/CSV-Reading/Employee-Master/Employee-Master.csv"

df = pd.read_csv(file_path)

cleansed_df = df.dropna(axis=0, how='all')

print(cleansed_df)

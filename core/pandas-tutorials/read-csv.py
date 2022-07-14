import pandas as pd

#Reading CSV file

file_path = "../../dataset/File-Handling/CSV-Reading/Employee-Master/Employee-Master.csv"

df = pd.read_csv(file_path)

print(df)
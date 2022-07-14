import pandas as pd

#Read Excel file

file_path = "../../dataset/File-Handling/Excel-Reading/Data-Generation.xlsx"

Excel_reading = pd.ExcelFile(file_path)

df = pd.read_excel(Excel_reading, 'EMPLOYEE-MASTER')

print(df)
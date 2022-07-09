import pandas as pd

if __name__ == "__main__":

    file_path = "../../dataset/File-Handling/Excel-Reading/Data-Generation.xlsx"

    Excel_reading = pd.ExcelFile(file_path)
    df1 = pd.read_excel(Excel_reading, 'EMPLOYEE-MASTER')
    df2 = pd.read_excel(Excel_reading, 'CLAIMS-MASTER')
    df3 = pd.read_excel(Excel_reading, 'SALARY-HISTORY')
    df4 = pd.read_excel(Excel_reading, 'CLAIMS-HISTORY')

    print(df1)
    print(df2)
    print(df3)
    print(df4)
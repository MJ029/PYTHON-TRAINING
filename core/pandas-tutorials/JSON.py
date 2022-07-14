import pandas as pd
import json

#convert CSV to JSON file

df = pd.read_csv ("../../dataset/File-Handling/CSV-Reading/Employee-Master/Employee-Master.csv")

json_file = json.dumps(f"{df}", sort_keys=False)

print(json_file)


import json
from pandas import json_normalize

#Create pandas dataframe from JSON

Data = '''
{
"Matches":
         [
         { "Player": "Surya", "Runs": 22,"Wickets":"4"},
         { "Player": "Rahul","Runs": 25,"Wickets":"3"},
         { "Player": "Ashok", "Runs": 23,"Wickets":"5"}
         ],
"status": ["ok"]
}
'''
print(Data)

dict = json.loads(Data)
df2 = json_normalize(dict['Matches'])
print(df2)

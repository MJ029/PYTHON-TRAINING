import pandas as pd
import numpy as np


#Create dataframe from numpy array

wickets = np.array([[1,1,1], [3,2,1], [4,1,2],
                   [1,2,3], [2,3,2], [1,1,1],
                   [3,4,1]])

players = ['Rahul', 'Dinesh', 'Dravid', 'Kohli', 'Shreyas', 'Balaji', 'Karthik']

matches = ['match1', 'match2', 'match3']

df = pd.DataFrame(data=wickets, index=players, columns=matches)

print(df)


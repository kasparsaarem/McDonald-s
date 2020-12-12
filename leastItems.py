
#Finding the least number of items to order to get one day's nutritional requirements

import pandas as pd

data = pd.read_csv("menu.csv")

calories = data["Calories"].max()

index = 0
for x in data.index:
    if(float(data.loc[x,'Calories']) == float(calories)):
        index = x

data.loc[[index]].values #All of the asked row's values

i = 0
for x in data.columns:
    print(x)
    print(data.loc[[index]].values[0][i])
    i = i + 1
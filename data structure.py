import pandas as pd

data = pd.read_csv("menu.csv")
print("Information about the dataset: ")
print("Columns: " + str(data.shape[1]))
print("Rows: " + str(data.shape[0]))
print()
print("Names of the columns (with indexes): ")
index = 0
for i in data.columns:
    print(str(index) + ".  " + i)
    index = index + 1
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
    
print()
print("The range of values and their distributions.")

for i in data.columns:
    print("Column: " + i + " - MAX: " + str(data[i].max())
          + ", MIN: " + str(data[i].min()))
    
print()

row = data.head(1)

for x in data.columns:
    print(x)
    print(row[x][0])
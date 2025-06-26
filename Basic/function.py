import pandas as pd
data = pd.Series([10,20,10,None,30,20,None,40], index = ['apple','mango','Banana','Graps','Strawberry','cherry','peach','orange'])

print("Original Series Is:")
print(data)

#head()
print("\nFirst 5 Elements Is:")
print(data.head())
#print(data.head(3)) #if we want to print first 3 element

#tail()
print("\nLast 5 Emement Is:")
print(data.tail())
print(data.tail(3))  #if we wnat to print last 3 element

#mean()
print("\nMean Of Value (Excluding Nan):")
print(data.mean())

#sum()
print("\nSum Of Value (Excluding Nan):")
print(data.sum())

#sort_values()
print("\nSorted By Values:")
print("Ascending:")
print(data.sort_values()) #ascending order
print("\nDescending:")
print(data.sort_values(ascending = False)) #descending order

#sort_index() (first priority gives capital font and after small font)
print("\nSorted By Index:")
print("Ascending:")
print(data.sort_index()) #ascending order
print("\nDescending:")
print(data.sort_index(ascending = False)) #descending order

#unique()
print("\nUnique Values:")
print(data.unique())

#value_counts()
print("\nFrequency Of Each Value:")
print(data.value_counts())

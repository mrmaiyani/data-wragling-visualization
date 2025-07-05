import pandas as pd

# Create A Sample Of Series
data = pd.Series(
    [10, 20, 10, None, 30, 20, None, 40],
    index=[
        "apple",
        "mango",
        "Banana",
        "Grapes",
        "Strawberry",
        "cherry",
        "peach",
        "orrange",
    ],
)
print("Original Series:")
print(data)

# head()
print("\nFirst 5 Elements:")
print(data.head())

# tail()
print("\nLast 5 Elements:")
print(data.tail())

# mean()
print("\nMean of values:")
print(data.mean())

# sum()
print("\nSum of values:")
print(data.sum())

# Sort_values()
print("\nSort by values(ascending order):")
print(data.sort_values())

# Sort_values()
print("\nSort by values(descending order):")
print(data.sort_values(ascending=False))

# sort_index()
print("\nSort by index(ascending order):")
print(data.sort_index())

# sort_index()
print("\nSort by index(descending order):")
print(data.sort_index(ascending=False))

# unique()
print("\nunique values:")
print(data.unique())

# value_counts()
print("\nFrequency of each value:")
print(data.value_counts())

# isnull()/notnull()
print("\nDetect missing data(isnull):")
print(data.isnull())
print(data[data.isnull()])

print("\nDetect non-missing data(notnull):")
print(data.notnull())
print(data[data.notnull()])

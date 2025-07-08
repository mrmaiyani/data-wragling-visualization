import pandas as pd

# creating a dataframe

# From a dictionary of lists(columns)
data = {
    "Name": ["DKP", "EDJ", "HRG"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "Chicago"],
}
df = pd.DataFrame(data)
print(df)

# Access Columns:
print("\n")
print(df["Name"])
print("\n")
print(df[["Name", "City"]])

# Access Rows:
print("\n")
print(df.loc[0])
print(df.iloc[0, 0])
print(df.loc[0, "Age"])
print(df.iloc[0, 1])

# Filtering & Conditional Selection
print("\n")
print(df[df["Age"] > 28])
print(df[(df["Age"] > 28) & (df["City"] == "LA")])  # tough multiple condition

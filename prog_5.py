import pandas as pd
import numpy as np

data = {
    "Name": ["DKP", "KJP", "HRG", "TSP", "EDJ", "PMP", np.nan],
    "Age": [25, 30, 35, np.nan, 45, 50, 32],
    "City": ["New York", "India", "New York", "Chicago", np.nan, "Chicago", "India"],
}

df = pd.DataFrame(data)

#1.head()
print("1.head():")
print(df.head())

#2.tail()
print("\n2.tail():")
print(df.tail())

#3.describe()
print("\n3.describe():")
print(df.describe())

#4.info()
print("\n4.info()")
print(df.info())

#5.sort_values(by='Age')-sort by 'Age'
print("\n5.sort by 'Age':")
print(df.sort_values(by='Age'))

#6.drop(columns=['City'])-drop city column
print("\n6.drop column of City:")
print(df.drop(columns=['City']))

#7.fillna(value)-fill missing value
print("\nfillna(value):")
print(df.fillna({'Age':df['Age'].mean(),'City':'Unknown','Name':'Missing'}))

#8.dropna()-drop rows with missing values
print("\n8.dropna():")
print(df.dropna())

#9.group by ('City')-Group by city and get average age
print("\n9.groupby('City')-mean.age:")
print(df.groupby('City')['Age'].mean())

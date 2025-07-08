import pandas as pd

df = pd.read_csv("CH1_DWV/stud_data.csv")
print(df)

df1 = pd.read_csv("CH1_DWV/stud_data.csv",index_col='name')
print("\n")
print(df1)

#display top 2 rows
print("\n")
print(df.head(2))

#display  last 2 rows
print("\n")
print(df.tail(2))

#display only name column
print("\n")
print(df['name'])

#display particular columns
print("\n")
print(df[['name','percentage']])

#display particular columns name and percentage with top 5 rows
print("\n")
print(df.head(5)[['name','percentage']]) 
print(df[['name','percentage']].head(5)) #same👆🏻

#display only 2nd rows
print("\n")
print(df.iloc[1])

#display particular row 2,5,8,9 with integer index
print("\n")
print(df.iloc[[2,5,8,9]])

#display particular row 2 to 7 using slicing
print("\n")
print(df.iloc[2:8])

#display 1 to 4 row with 1 and 2 column
print("\n")
print(df.iloc[1:5,1:3])

#display particular row with particular index
print("\n")
print(df1.loc['Neha Singh'])

#display multiple row with particular name index
print("\n")
print(df1.loc[['Priya Verma','Sneha Nair','Ravi Desai','Karan Sethi']])

#display particular row with gender male
print("\n")
print(df.loc[df.gender == 'Male'])

#display top 5 rows with gender male
print("\n")
print(df.loc[df.gender == 'Male'].head())
print(df[df.gender == 'Male'].head())

#display particular rows with >90 percentage
print("\n")
print(df[df.percentage>'90'])

#display sum of total column
print("\n")
print("Sum Of Total:",df.total.sum())

#multiple condition
print("\n")
print(df.loc[(df.gender == 'Female') & (df.percentage>'90')])

#display name of 2nd row
print("\n")
print('Student Name:',df.iloc[1]['name'])

#display percentage of particular student(nisha roy)
print("\n")
print('Nisha Roy\'s Percentage:',df1.loc['Nisha Roy']['percentage'])

#Average of male students.
print("\n")
total1 = df[df.gender == 'Male']['total'].sum()
n = df[df.gender == 'Male']['total'].count()
print("tatal n")
print("👇🏻👇🏻")
print(total1,n)
print("\n")
print("Average:",total1/n)
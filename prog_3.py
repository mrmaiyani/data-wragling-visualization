import pandas as pd

# creating a dataframe

# From a dictionary of lists(columns)
data = {
    'Name':['DKP','EDJ','HRG'],
    'Age':[25,30,35],
    'City':['NY','LA','Chicago']
}
df = pd.DataFrame(data)
print(df)
print("\n")

# From a list of dictionaries(rows)
data = [
    {'Name':'KJP','Age':25,'City':'NY'},
    {'Name':'TKP','Age':30,'City':'LA'},
    {'Name':'SBP','Age':35,'City':'Chicago'}
]
df2 = pd.DataFrame(data)
print(df2)
print("\n")

# From a list of list
data = [
    ['DBP',25,'NY'],
    ['BKP',30,'LA'],
    ['KMP',35,'Chicago']
]
df3 = pd.DataFrame(data,columns = ['Name','Age','City'])
print(df3)

# From a dictionary of list using index attribute
data = {
    'RollNo':[1,2,3,4,5],
    'Name':['Pooja','Aarti','Suraj','Aryan','Megha']
}
df4 = pd.DataFrame(data,index = ['s1','s2','s3','s4','s5'])
print(df4)
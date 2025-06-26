import pandas as pd
import numpy as np

data = {
    'name': ['DKP','KJP','HRG','TSP','EDJ','PMP',np.nan],
    'age':[25,30,35,np.nan,45,50,32],
    'city':['New York','India','New York','Chicago',np.nan,'Chicago','India']
    }

'''data = [
    {'name':'KJP','age':25,'city':'NY'},
    {'name':'TKP','age':30,'city':'LA','gender':'male'},
    {'name':'SBP','age':35,'city':'Chicago'}
    ]'''

print(data)
df = pd.DataFrame(data)
print(df)

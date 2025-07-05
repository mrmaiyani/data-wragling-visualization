import pandas as pd

# 1.Create Series 
'''
# From A List Or Array
S = pd.Series([10,20,30,40,50,60,70,80,90,100])

# With Custom Index
S = pd.Series([10,20,30,40,50,60,70,80,90,100],index = ['1','2','3','4','5','6','7','8','9','10'])

# From A Dictionary
S = pd.Series({'1':100,'2':200,'3':300,'4':400,'5':500,'6':600,'7':700,'8':800,'9':900,'10':1000})

# Scalar With Index
S = pd.Series(300,index = ['1','2','3','4','5','6','7','8','9','10'])

print(S)
'''

# 2.Series Components
'''
S = pd.Series([100,200,300,400,500,600,700,800,900,1000],index = ['a','b','c','d','e','f','g','h','i','j'])
print(S)

print(S.index)
print(S.values)
print(S.dtype)
print(S.shape)
'''

# 3.Accessing Elements
'''
S = pd.Series([100,200,300,400,500,600,700,800,900,1000],index = ['a','b','c','d','e','f','g','h','i','j'])
print(S)

print(S['a']) #label access
print(S[8]) #positional access
print(S[['a','j']])
'''

# 4.Filtering & Boolean Indexing
'''
S = pd.Series([100,200,300,400,500,600,700,800,900,1000],index = ['a','b','c','d','e','f','g','h','i','j'])
print([S > 500]) #Boolean Indexing
print(S[S > 500]) #filtering
'''
























import pandas as pd
s = pd.Series([10,20,30])     
s = pd.Series([10,20,30], index=['a','b','c'])
#s = pd.Series({'a':100,'b':200,'c':300})     
#s = pd.Series(5,index = ['a','b','c'])
#s = pd.Series([100,200,300],index = ['a','b','c'])

print(s)
print(s.index)
print(s.values)
print(s.dtype)
print(s.shape)
print(s['c'])
print(s[s<=20])

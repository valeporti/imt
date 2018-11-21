import pandas as pd
import numpy as np

T = pd.Series([1,3,5,np.nan,6,8])

print(T)

S = pd.Series([1,3,5,np.nan,6,8],index=[10,50,111,225,3,16])

print(S)

D = dates = pd.date_range('20130101', periods=6)

print(D)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))  

print(df)

# ask for a data frame
print(df['20130102':'20130104'])

df2 = pd.DataFrame({ 'A' : 1.,
  'B' : pd.Timestamp('20130102'),
  'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
  'D' : np.array([3] * 4,dtype='int32'),
  'E' : pd.Categorical(["test","train","test","train"]),
  'F' : 'foo' })

print(df2)

df2.sort_values(by='B')

print(df2)


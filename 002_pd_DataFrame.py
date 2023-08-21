# -------------------------------------------
# Deal with NaN
# -------------------------------------------

>>> import pandas as pd
>>> df = pd.DataFrame([{'a':1, 'b':2},{'b':3, 'c':4}])
>>> df
     a  b    c
0  1.0  2  NaN
1  NaN  3  4.0
>>> df.fillna(0)
     a  b    c
0  1.0  2  0.0
1  0.0  3  4.0

>>> data = pd.Series(['a', 'b', 'c'], index=[1,3,5])
>>> data
1    a
3    b
5    c
dtype: object
>>> data[1]      # explicit index use loc
'a'
>>> data.loc[1]   # explicit index    
'a'
>>> data[0:2]      # implicit index use iloc
1    a
3    b
dtype: object
>>> data.iloc[[0,1]]  # implicit index
1    a
3    b
dtype: object


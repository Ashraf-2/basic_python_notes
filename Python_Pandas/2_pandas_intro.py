import pandas as pd

data = [10,20,30,40,50]
s = pd.Series(data)
print(s)
print(s[2])     # accessing value by label
print(s.iloc[3])    # accessing value by position

print(s[1:4])       # accessing multiple values using range (index 1 to before 4th)
print("mean: ", s.mean())
print("std: ", s.std())
print("isNull : ", s.isnull())
print("sort values : ", s.sort_values())
print("index: ",s.index)
print("size: ",s.size)
print("values type: ",type(s.values))
print("values: ",s.values)

import pandas as pd
ser = pd.Series([1,2,3,4,5])
print(ser)


a = [1,3,4,5,56,]
res = pd.Series(a,index = ["x","y","z","w","e"])
print(res)
print(res[1])
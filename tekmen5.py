#Dealing with NaN values in dataframes


import numpy as np
import pandas as pd


items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

df = pd.DataFrame(items, index = ["store1", "store2", "store3"])

print(df, "\n"*3)


times_NaN = df.isnull().sum()
# print(type(times_NaN)) =  <class 'pandas.core.series.Series'>

times_NaN = df.isnull().sum().sum()
print ("how many NaN's? : ", times_NaN)

print("\n\n number of non-NaN items : ", df.count())
#also df.count().sum()


print("\n\n drop rows or columns whit NaN values : \n\n", df.dropna(axis = 1))

print("\n\n fill NaNs with True \n\n", df.fillna(True))

#axis = 0 süütun bazında interpolasyon yap
print("\n\n interpolated NaNs : \n\n", df.interpolate(method = "linear", axis = 0))


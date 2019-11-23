
"""
Simple linear regression model, uses stock data from Quandl, from Sentdex ML tutorials.
Original source : https://www.youtube.com/watch?v=r4mwkS2T9aI&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=5&t=0s
"""

"""
Note : Trains linear regression model but how will we use this model to make predictions?
"""


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import quandl

from sklearn import preprocessing, svm
from sklearn import model_selection
from sklearn.linear_model import LinearRegression


#get data from Quandl database
df = quandl.get("WIKI/GOOGL")

"""
for column in df.columns:
print(column)
"""

#adjust df columns so that we will use only useful columns
df = df[["Adj. Open", "Adj. High","Adj. Low","Adj. Close","Adj. Volume"]]
df["HL_PCT"] = df["Adj. High"] - df["Adj. Close"] / df["Adj. Close"] * 100
df["PCT_change"] = df ["Adj. Close"] - df["Adj. Open"] / df["Adj. Open"] * 100

df = df[["Adj. Close", "PCT_change", "HL_PCT", "Adj. Volume"]]

#fill the Nans with -99999
df.fillna(-99999, inplace=True)

forecast_col = "Adj. Close"     #???

forecast_out = int(math.ceil(0.01*len(df)))     #shift columns upward by %1
df["label"] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)     #drop NaN valued rows (%1 of rows from bottom)

#split our data 
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)

clf = LinearRegression()      #initialize model
clf.fit(X_train, y_train)     #train model with X_train and y_train
accuracy = clf.score(X_test, y_test)     #find accuracy on test set

print(accuracy)





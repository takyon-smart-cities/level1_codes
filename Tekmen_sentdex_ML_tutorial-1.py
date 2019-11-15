import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import quandl

df = quandl.get("WIKI/GOOGL")

"""
#Just to try syntax of pandas
#for column in df.columns:
#    print(column)
#print(df[["Adj. Open",]])
#print(df)
"""


#data wraggling for logistic regression
df = df[["Adj. Open", "Adj. High","Adj. Low","Adj. Close","Adj. Volume"]]
df["HL_PCT"] = df["Adj. High"] - df["Adj. Close"] / df["Adj. Close"] * 100
df["PCT_change"] = df ["Adj. Close"] - df["Adj. Open"] / df["Adj. Open"] * 100

df = df[["Adj. Close", "PCT_change", "HL_PCT", "Adj. Volume"]]
#print(df)



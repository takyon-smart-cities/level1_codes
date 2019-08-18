#pandas kütüphanesi basics çalışması


import pandas as pd


groceries = pd.Series(data = [14,5,3], index = ["banana", "apple","cucumber"])
dc ={"a" : 1,
    "b" : 2,}

dc["c"] = 3



seri = pd.Series(dc)
print("seri : ", seri)



data = {"sayılar": seri,
        "on katı" : pd.Series(data = [10,20,30], index = [*dc])}
df = pd.DataFrame(data)

print("frame : ", frame)



data = {"integers" : range(3),
       "floats" : map(float, range(3))}

df = pd.DataFrame(data, index = ["l1","l2","l3"])
print("df : ", df)



print("print just integers :\n\n", df[["integers"]])
print("print just l1 and l3 \n\n", df.loc[["l1","l3"]])
#demek ki loc metoduyla key olarak satır giriyoruz,
#normal key girdiğimizde sütun alıyor

print("l3 integer : ", df["integers"]["l3"])


#l3 ü değiştirelim
df.loc["l3"] = [3, 4.3]


#yeni satır ekleyelim
new_nums = [{"integers" : 5 , "floats" : 5.6}]
new_df = pd.DataFrame(new_nums, index = ["l4"])
print("new_df : ", new_df)
df = df.append(new_df)


df = df.rename(index = {"l1": "label1"})



import pandas as pd

data={
    'Name':["Player_A","Player_B","Player_c"],
    'Age':[25,30,35]
}

df=pd.DataFrame(data)
print(df)

age_series=pd.Series([25,30,35],index=["PlayerA","PlayerB","PlayerC"])
print(age_series)

data={
    'Name':["Alice","Bob","Charlie","David","Eva"],
    'Age':[24,27,22,32,29],
    'City':['New York','Los Angeles','Chicago','Houston','Phoenix']
}

df=pd.DataFrame(data)

print("First three rows using head:")
print(df.head(3))

print("\nLast two rows using tail")
print(df.tail(2))

print("\nDataFrame summary using info:")
print(df.info())
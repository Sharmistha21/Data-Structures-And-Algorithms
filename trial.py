import pandas as pd

data = {
    'Item': ['Cake', 'Cake', 'Bread', 'Pastry', 'Cake'],
    'Flavor': ['Chocolate', 'Vanilla', 'Whole Wheat', 'Strawberry', 'Chocolate'],
    'Price': [250, 220, 80, 120, 250]
}

df = pd.DataFrame(data)
print(df)

grouped=df.groupby('Item')
print(grouped)

print(df.groupby('Item')['Price'].sum())
print(df.groupby(['Item','Flavor'])['Price'].sum())





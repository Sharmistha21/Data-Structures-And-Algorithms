import pandas as pd
import numpy as np

df=pd.DataFrame({'Col1':[1,2,np.nan],'Col2':[3,np.nan,np.nan]})
print(df.isnull())

df.fillna(0,inplace=True)
print(df)

#drop values

df = pd.DataFrame({
    'A': [100, np.nan, np.nan, 95],
    'B': [30, np.nan, 45, 56],
    'C': [52, np.nan, 80, 98],
    'D': [np.nan, np.nan, np.nan, 65]
})


print("\nDrop rows with at least 1 NaN:\n", df.dropna())
print("\nDrop rows where all values are NaN:\n", df.dropna(how='all'))
print("\nDrop columns with at least 1 NaN:\n",df.dropna(axis=1))

print("\nDrop rows with at least 1 NaN:\n",df[df.notna().all(axis=1)])
print("\nDrop rows where all values are NaN:\n",df[df.notna().any(axis=1)])
print("\nDrop columns with at least 1 NaN:\n",df.loc[:,df.notna().all()])



import pandas as pd


data1 = {
    'Name': ['Alice', 'Charlie', 'Edward', 'Grace'],
    'Years_Experience': [2, 3, 4, 6]
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['Alice', 'Charlie', 'Frank', 'Grace'],
    'Role': ['Manager', 'Analyst', 'Developer', 'HR']
}
df3 = pd.DataFrame(data2)


df_merged_inner=pd.merge(df1,df3,on='Name',how='inner')
df_merged_outer=pd.merge(df1,df3,on='Name',how='outer')

print(df_merged_inner)
print(df_merged_outer)

df = pd.DataFrame({
    'Name': ['Alice', 'Charlie', 'Edward', 'Grace'],
    'Years_Experience': [2, 3, 4, 6],
    'Role': ['Manager', 'Analyst', 'Developer', 'HR']
})


new_df = pd.DataFrame({
    'Name': ['John', 'Lily'],
    'Years_Experience': [5, 3],
    'Role': ['Designer', 'Developer']
})


concatenated_df=pd.concat([df,new_df],ignore_index=True)
print(concatenated_df)

Names = {'FirstName':['Suzie','Emily','Mike','Robert'],
         'LastName':['Bates','Edwards','Curry','Frost']}
 
# creating a dataframe from dictionary
df = pd.DataFrame(Names, columns=['FirstName','LastName'])
print(df)

df['Name']=df['FirstName'].map(str)+' '+df['LastName'].map(str)
print(df)
 


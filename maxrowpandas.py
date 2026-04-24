import pandas as pd
import numpy as np

# data of 2018 drivers world championship
dict1 = {'Driver': ['Hamilton', 'Vettel', 'Raikkonen',
                    'Verstappen', 'Bottas', 'Ricciardo',
                    'Hulkenberg', 'Perez', 'Magnussen',
                    'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                    'Grosjean', 'Gasly', 'Vandoorne',
                    'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],

         'Points': [408, 320, 251, 249, 247, 170, 69, 62, 56,
                    53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],

         'Age': [33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                 22, 21, 32, 22, 26, 28, 20, 29, 23]}

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
print(df.head(10))

print(df.max())

print(df[df.Points==df.Points.max()])
print(df.Age.max())

print(df[df.Age==df.Age.min()])

data={'Name':['Alice','Bob','Charlie'],'Age':[25,30,45],'Score':[85,90,78]}
df=pd.DataFrame(data)
filtered_df=df[df['Age']>28]
print(filtered_df)

filtered_df=df[df['Age'].isin([25,45])]
print(filtered_df)

filtered_df=df.query('Age>30 and Score<90')
print(filtered_df)

data = [['John', 8, 7, 6, 5], ['Paul', 8, 3, 6, 4],
        ['Juli', 9, 10, 9, 9], ['Geeta', 9, 5, 4, 4]]

# Create the pandas DataFrame
df = pd.DataFrame(
    data, columns=['Name', 'Class', 'English', 
                   'Maths', 'History'])

# print dataframe.
print(df)

df1=df.loc[(df['English']>6) & (df['Maths']>6)]
print(df1)

df1=df.loc[((df['English']>6) & (df['Maths']>4)),['Name','Class']]
print(df1)

dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

print(dataFrame.loc[(dataFrame['Salary']>=10000) & (dataFrame['Age']<40) & (dataFrame['JOB'].str.startswith('D')),['Name','JOB']])
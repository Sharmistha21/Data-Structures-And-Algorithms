import numpy as np

zeros_array=np.zeros((2,3))
print(zeros_array)

import numpy as np
import pandas as pd

students = [
    ('Ankit', 22, 'Up', 'Geu'),
    ('Ankita', np.nan, 'Delhi', np.nan),
    ('Rahul', 16, 'Tokyo', 'Abes'),
    ('Simran', 41, 'Delhi', 'Gehu'),
    ('Shaurya', np.nan, 'Delhi', 'Geu'),
    ('Shivangi', 35, 'Mumbai', np.nan),
    ('Swapnil', 35, np.nan, 'Geu'),
    (np.nan, 35, 'Uk', 'Geu'),
    ('Jeet', 35, 'Guj', 'Gehu'),
    (np.nan, np.nan, np.nan, np.nan)
]

details = pd.DataFrame(
    students,
    columns=['Name', 'Age', 'Place', 'College'],
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k']
)

print("Boolean DataFrame:\n", details.isnull())
print("\nCount of NaN in each column:\n", details.isnull().sum())
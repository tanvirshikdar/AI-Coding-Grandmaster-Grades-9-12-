import numpy as np
import pandas as pd

d1 = {'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'], 'ID': [1, 2, 3, 4], 'Salary': [100, 200, np.nan, pd.NaT],
      'Role': ['CEO', None, pd.NaT, pd.NaT]}

df = pd.DataFrame(d1)

print("--- Full DataFrame ---")
print(df)

print("\n--- Head (First 2) ---")
print(df.head(2))

print("\n--- Tail (Last 2) ---")
print(df.tail(2))

print("\n--- Null Count ---")
print(df.isnull().sum())

print("\n--- Info ---")
df.info()

print("\n--- Dropna (Rows) ---")
df1 = df.dropna()
print(df1)

print("\n--- Dropna (Columns) ---")
df2 = df.dropna(axis=1)
print(df2)

df['Salary'] = df['Salary'].fillna('300')

print("\n--- After Salary Fill ---")
print(df)

df['Role'] = df['Role'].fillna('CEO')

print("\n--- Final DataFrame ---")
print(df)
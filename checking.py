import pandas as pd

df = pd.read_csv("merege.csv")
print(df.isnull().sum())

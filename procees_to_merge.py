import pandas as pd

files = ["part_1.csv", "part_2.csv", "part_3.csv"]

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
df.to_csv("merege.csv", index=False)

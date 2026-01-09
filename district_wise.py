import pandas as pd

df = pd.read_csv("merege.csv")
df["district"] = (
    df["district"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
)
df = df[~df["district"].str.isnumeric()]
district_user_count = (
    df.groupby("district")
    .size()
    .reset_index(name="user_count")
    .sort_values(by="user_count", ascending=True)
)

print(district_user_count)
district_user_count.to_csv("district_wise_usercount.csv")

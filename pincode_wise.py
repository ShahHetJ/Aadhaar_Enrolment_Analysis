import pandas as pd

df = pd.read_csv("merege.csv")

df["pincode"] = df["pincode"].astype(str).str.strip()

df = df[df["pincode"].str.match(r"^\d{6}$", na=False)]

pincode_user_count = (
    df.groupby("pincode")
    .size()
    .reset_index(name="user_count")
    .sort_values(by="user_count", ascending=True)
)

print(pincode_user_count)

pincode_user_count.to_csv("pincode_user_count.csv")

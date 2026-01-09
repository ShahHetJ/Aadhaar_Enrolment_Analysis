import pandas as pd

df = pd.read_csv("merege.csv")

df["state"] = (
    df["state"].astype(str).str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
)
df = df[~df["state"].str.isnumeric()]

state_map = {
    # Odisha
    "orissa": "odisha",
    # Andaman
    "andaman & nicobar islands": "andaman and nicobar islands",
    # Dadra / Daman (merged UT)
    "dadra & nagar haveli": "dadra and nagar haveli and daman and diu",
    "dadra and nagar haveli": "dadra and nagar haveli and daman and diu",
    "daman & diu": "dadra and nagar haveli and daman and diu",
    "daman and diu": "dadra and nagar haveli and daman and diu",
    "the dadra and nagar haveli and daman and diu": "dadra and nagar haveli and daman and diu",
    # West Bengal
    "west bangal": "west bengal",
    "westbengal": "west bengal",
}

df["state"] = df["state"].replace(state_map)

df["state"] = df["state"].replace({"jammu & kashmir": "jammu and kashmir"})


state_user_count = (
    df.groupby("state")
    .size()
    .reset_index(name="user_count")
    .sort_values(by="user_count", ascending=True)
)

print(state_user_count)
# ouptut in state user_count.csv

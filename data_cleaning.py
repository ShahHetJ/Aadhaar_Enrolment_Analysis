import pandas as pd
import difflib
import re

# 1. Load your dataset
df = pd.read_csv("district_wise_usercount.csv")


# --- Step 1: Basic Cleanup ---
# Removes special characters (*, ?) and standardizes whitespace
def basic_clean(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()
    # Replace non-alphanumeric chars (like * or ?) with space
    text = re.sub(r"[^\w\s]", " ", text)
    # Collapse multiple spaces into one
    text = " ".join(text.split())
    return text


df["district_clean"] = df["district"].apply(basic_clean)

# --- Step 2: Dynamic Clustering (The "No Predefined List" Logic) ---
# This finds "clusters" of similar names without knowing the correct one in advance.

# Get unique names and sort by frequency (so the most common spelling becomes the "Master")
counts = df["district_clean"].value_counts()
sorted_names = counts.index.tolist()

canonical_names = []
name_mapping = {}

for name in sorted_names:
    # Check if this name is similar to any name we've already accepted
    # cutoff=0.85 means "85% similar". Adjust this up/down for strictness.
    matches = difflib.get_close_matches(name, canonical_names, n=1, cutoff=0.85)

    if matches:
        # It's a typo/duplicate of an existing group! Map it.
        name_mapping[name] = matches[0]
    else:
        # It's a new, unique name. Add to our "Master" list.
        canonical_names.append(name)
        name_mapping[name] = name

# Apply the fixes
df["district_fixed"] = df["district_clean"].map(name_mapping).str.title()

# Save the result
df.to_csv("cleaned_district_usercount.csv", index=False)

# Display some examples of what was fixed
changes = df[df["district_clean"] != df["district_fixed"].str.lower()]
print(changes[["district", "district_fixed"]].head(10))

import pandas as pd
df = pd.read_csv("data/raw/student.csv")
df = df.drop_duplicates()
for c in df.columns:
    if df[c].dtype == "object":
        df[c] = df[c].fillna(df[c].mode()[0])
    else:
        df[c] = df[c].fillna(df[c].median())
df.to_csv("data/processed/student_clean.csv", index=False)
print(df.shape)


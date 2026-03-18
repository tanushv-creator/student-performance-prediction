import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/raw/student-mat.csv", sep=";")

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

# Save processed copy
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/student_clean.csv", index=False)
print("\nClean data saved to data/processed/student_clean.csv")
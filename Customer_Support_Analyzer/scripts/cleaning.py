import pandas as pd
import csv

df = pd.read_csv("data/support_raw.csv", low_memory=False)


df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
print("Fixed columns:", df.columns.tolist())

# Clean text
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.replace(r'\r\n|\n|\r', ' ', regex=True)
    df[col] = df[col].str.replace('"', "'", regex=False)

df['customer_age'] = pd.to_numeric(df['customer_age'], errors='coerce').fillna(0).astype(int)
df['customer_satisfaction_rating'] = pd.to_numeric(df['customer_satisfaction_rating'], errors='coerce').fillna(0)

df.to_csv("data/cleaned_support.csv", index=False, quoting=csv.QUOTE_ALL)
print(f"SUCCESS shape {df.shape}")
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\sufiyan\Downloads\archive\dirty_cafe_sales.csv")

# Preview the data
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
print(f"Duplicate rows: {df.duplicated().sum()}")

# -------------------------------
# Handling Missing & Incorrect Data
# -------------------------------

# Fill missing 'Location' with a placeholder
df["Location"].fillna("Unknown", inplace=True)

# Convert numeric columns to proper types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Fill missing numeric values using median
df["Quantity"].fillna(df["Quantity"].median(), inplace=True)
df["Price Per Unit"].fillna(df["Price Per Unit"].median(), inplace=True)

# Calculate missing 'Total Spent' using Quantity * Price
df["Total Spent"].fillna(df["Quantity"] * df["Price Per Unit"], inplace=True)

# Fill missing categorical columns with placeholders
df["Item"].fillna("Unknown", inplace=True)
df["Payment Method"].fillna("Unknown", inplace=True)

# Fix and format 'Transaction Date'
df["Transaction Date"].fillna("01-01-2000", inplace=True)
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce", dayfirst=True)

# Print final missing value counts
print(df.isnull().sum())

# -------------------------------
# Standardizing Text Data
# -------------------------------

df["Item"] = df["Item"].str.title().str.strip()
df["Payment Method"] = df["Payment Method"].str.title().str.strip()
df["Location"] = df["Location"].str.title().str.strip()

# -------------------------------
# Clean Column Names & Data Types
# -------------------------------

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df["quantity"] = df["quantity"].astype(int)
df["price_per_unit"] = df["price_per_unit"].astype(float)
df["total_spent"] = df["total_spent"].astype(float)

# Final preview
print(df.head())

import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# 1. Identify and handle missing values
print("Missing values before cleaning:\n", df.isnull().sum())
df = df.fillna({'director': 'Unknown', 'cast': 'Unknown', 'country': 'Unknown'})  #replacements
df = df.dropna(subset=['date_added', 'rating'])  # Drop rows where these key columns are missing

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Standardize text values (example: country, rating)
df['country'] = df['country'].str.strip().str.title()
df['rating'] = df['rating'].str.upper().str.replace(" ", "")

# 4. Convert date formats to consistent type
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', dayfirst=True)

# 5. Rename column headers
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 6. Check and fix data types
if 'release_year' in df.columns:
    df['release_year'] = df['release_year'].astype(int, errors='ignore')

# 7. new file of cleaned dataset
output_filename = "cleaned_netflix_data.csv"
df.to_csv(output_filename, index=False)
print(f"\n✅ Cleaned dataset saved as: {output_filename}")

# Display cleaned info
print("\nCleaned Data Overview:")
print(df.info())
print("\nSample Data:")
print(df.head())

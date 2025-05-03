import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

df = pd.read_csv('data/raw/raw_data.csv')

# Replace "NA" strings and convert to float
df['Humidity'] = df['Humidity'].replace("NA", 50).astype(float)

# Fill any missing numeric values before scaling
df[['Temperature', 'Humidity', 'Wind Speed']] = df[['Temperature', 'Humidity', 'Wind Speed']].fillna(0)

# Normalize
scaler = MinMaxScaler()
df[['Temperature', 'Humidity', 'Wind Speed']] = scaler.fit_transform(
    df[['Temperature', 'Humidity', 'Wind Speed']])

# Just in case: recheck for NaNs post-scaling
df = df.fillna(0)

os.makedirs('data/processed', exist_ok=True)
df.to_csv('data/processed/processed_data.csv', index=False)

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

df = pd.read_csv('data/processed/processed_data.csv')
X = df[['Humidity', 'Wind Speed']]
y = df['Temperature']

model = LinearRegression()
model.fit(X, y)

# Save model
os.makedirs('model', exist_ok=True)
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

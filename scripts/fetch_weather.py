import requests
import csv
from datetime import datetime
import os

# Islamabad coordinates
lat, lon = 33.6844, 73.0479

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
response = requests.get(url).json()
weather = response["current_weather"]

data = {
    "Temperature": weather["temperature"],
    "Wind Speed": weather["windspeed"],
    "Humidity": "NA",  # Not provided by Open-Meteo
    "Weather Condition": weather["weathercode"],
    "Date and Time": datetime.now().isoformat()
}

# Ensure folder exists
os.makedirs('data/raw', exist_ok=True)

file_path = 'data/raw/raw_data.csv'
write_mode = 'a' if os.path.exists(file_path) else 'w'

with open(file_path, write_mode, newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data.keys())
    if write_mode == 'w':
        writer.writeheader()
    writer.writerow(data)

print("Weather data appended successfully.")

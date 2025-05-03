# Weather Data Engineering Pipeline (Airflow + DVC)

This project automates the collection, preprocessing, and modeling of weather data using:

- 📡 Live data from **Open-Meteo API**
- ⚙️ Workflow orchestration with **Apache Airflow**
- 📦 Dataset + model versioning with **DVC**
- 🤖 Simple ML model using **Linear Regression**

---

## 🔁 Pipeline Workflow

### 1. Fetch Data
- Collects temperature, wind speed, humidity, and weather condition
- Saves to `data/raw/raw_data.csv`

### 2. Preprocess
- Replaces missing values
- Normalizes data using `MinMaxScaler`
- Saves to `data/processed/processed_data.csv`

### 3. Train Model
- Linear regression model to predict **temperature**
- Saves model to `model/model.pkl`

---

## 🚀 Tools Used

| Tool | Purpose |
|------|---------|
| Apache Airflow | Automates fetch → preprocess workflow |
| DVC | Version control for data + model |
| Scikit-learn | Machine learning model |
| Pandas | Data manipulation |
| Git | Version control for code |

---

## 🧪 How to Run

1. Clone this repo  
2. Set up virtual environment and install requirements:

```bash
python3 -m venv airflow_venv
source airflow_venv/bin/activate
pip install -r requirements.txt

## Airflow Integration

The project is also integrated with Apache Airflow. DAG `weather_pipeline` orchestrates:

- `fetch_weather` – fetches live weather data
- `preprocess_data` – cleans and scales it
- `train_model` – trains a regression model

Access Airflow at: [http://localhost:8081](http://localhost:8081)

Start with:
```bash
airflow scheduler &
airflow webserver --port 8081 &

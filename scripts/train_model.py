import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os
import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set the MLflow tracking URI (replace with your actual URI if needed)
mlflow.set_tracking_uri('http://localhost:5000')

# Load processed data
df = pd.read_csv('data/processed/processed_data.csv')
X = df[['Humidity', 'Wind Speed']]
y = df['Temperature']

# Start an MLflow run to track the experiment
with mlflow.start_run():
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X, y)

    # Predictions
    predictions = model.predict(X)

    # Calculate metrics
    mse = mean_squared_error(y, predictions)
    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)

    # Log metrics to MLflow
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2_score", r2)

    # Log the trained model to MLflow
    mlflow.sklearn.log_model(model, "weather_model")

    # Save the model locally using pickle
    os.makedirs('model', exist_ok=True)
    with open('model/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    # Optionally log parameters, for example:
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("features", "Humidity, Wind Speed")

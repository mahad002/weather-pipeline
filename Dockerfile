FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV AIRFLOW_HOME=/app/airflow
ENV MLFLOW_TRACKING_URI=http://localhost:5000

# Create necessary directories
RUN mkdir -p /app/data/raw /app/data/processed /app/mlruns

# Expose ports
EXPOSE 8081 5000

# Set the entrypoint
ENTRYPOINT ["python", "scripts/main.py"] 
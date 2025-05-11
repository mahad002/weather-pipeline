# Base image with Python 3.10
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose necessary ports
EXPOSE 8081  
EXPOSE 8082 

# Set the entry point to run Airflow Scheduler and Webserver on port 8081
CMD ["airflow", "webserver", "--port", "8081"]

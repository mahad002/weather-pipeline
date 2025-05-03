from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 5, 1),
    'catchup': False
}

with DAG('weather_pipeline', default_args=default_args, schedule_interval=None) as dag:
    fetch = BashOperator(
        task_id='fetch_weather',
        bash_command='python3 /home/mahad/weather-pipeline/scripts/fetch_weather.py'
    )

    preprocess = BashOperator(
        task_id='preprocess_data',
        bash_command='python3 /home/mahad/weather-pipeline/scripts/preprocess.py'
    )

    train = BashOperator(
        task_id='train_model',
        bash_command='python3 /home/mahad/weather-pipeline/scripts/train_model.py'
    )

    fetch >> preprocess >> train

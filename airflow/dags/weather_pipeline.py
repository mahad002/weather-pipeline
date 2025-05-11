from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def create_dag():
    dag = DAG(
        'weather_pipeline',
        default_args=default_args,
        description='Weather data processing and model training pipeline',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2024, 1, 1),
        catchup=False,
    )

    # Data Collection Task
    collect_data = DockerOperator(
        task_id='collect_weather_data',
        image='weather-pipeline:latest',
        command='python scripts/collect_data.py',
        network_mode='bridge',
        dag=dag,
    )

    # Data Processing Task
    process_data = DockerOperator(
        task_id='process_weather_data',
        image='weather-pipeline:latest',
        command='python scripts/process_data.py',
        network_mode='bridge',
        dag=dag,
    )

    # Model Training Task
    train_model = DockerOperator(
        task_id='train_weather_model',
        image='weather-pipeline:latest',
        command='python scripts/train_model.py',
        network_mode='bridge',
        dag=dag,
    )

    # Model Evaluation Task
    evaluate_model = DockerOperator(
        task_id='evaluate_weather_model',
        image='weather-pipeline:latest',
        command='python scripts/evaluate_model.py',
        network_mode='bridge',
        dag=dag,
    )

    # Set task dependencies
    collect_data >> process_data >> train_model >> evaluate_model

    return dag

dag = create_dag() 
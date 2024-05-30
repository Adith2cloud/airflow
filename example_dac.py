from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 30),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@once',  # Run once immediately when triggered
)

# Define tasks
start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

# Define the task dependencies
start_task >> end_task

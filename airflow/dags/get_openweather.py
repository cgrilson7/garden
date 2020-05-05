from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
# from etl_functions.etl import etl

dag = DAG(
    'get_current_weather',
    default_args={
        "owner": "me",
        "start_date": datetime(2020, 5, 4)
    },
    schedule_interval="*/5 * * * *",
    catchup=False
)

bash_task = BashOperator(
    dag=dag,
    task_id='etl',
    bash_command='python3 /Users/CW/garden/etl.py'
)

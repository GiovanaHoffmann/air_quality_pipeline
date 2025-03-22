from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess
import logging
from airflow.exceptions import AirflowException

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'air_quality_etl',
    default_args=default_args,
    schedule_interval='@hourly',
)

def run_etl():
    try:
        subprocess.run(["python3", "main.py"], check=True)
        logging.info("Pipeline ETL executado com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar o pipeline: {e}")
        raise AirflowException(f"Erro ao executar o pipeline: {e}")

task = PythonOperator(
    task_id='run_etl_script',
    python_callable=run_etl,
    dag=dag,
)
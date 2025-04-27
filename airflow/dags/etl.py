from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess
import logging
from airflow.exceptions import AirflowException
import os

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(hours=1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False # evita execuções retroativas
}

dag = DAG(
    'air_quality_etl',
    default_args=default_args,
    schedule_interval='@hourly',
    max_active_runs=1 # Garante que apenas uma instância da DAG esteja ativa por vez
)

def run_etl():
    try:
        subprocess.run(["python", "/opt/main.py"], check=True)
        logging.info("Pipeline executado com sucesso!")
    except Exception as e:
        logging.error(f"Erro no pipeline: {str(e)}")
        raise AirflowException(f"Erro no pipeline: {str(e)}")

task = PythonOperator(
    task_id='run_etl_script',
    python_callable=run_etl,
    dag=dag,
)
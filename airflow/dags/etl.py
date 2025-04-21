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
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False
}

dag = DAG(
    'air_quality_etl',
    default_args=default_args,
    schedule_interval='@hourly',
)

def run_etl():
    """
    try:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
        main_path = os.path.join(base_dir, 'main.py')
        subprocess.run(["python3", main_path], check=True)
    except subprocess.CalledProcessError as e:
        raise AirflowException(f"Erro ao executar o pipeline: {e}")
    """
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
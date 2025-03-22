from extract import fetch_data
from transform import transform_data
from load import create_table, load_data
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_etl():
    logging.info("Iniciando pipeline ETL...")
    create_table()  # Garante que a tabela existe
    raw_data = fetch_data()
    df = transform_data(raw_data)
    load_data(df)
    logging.info("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    run_etl()
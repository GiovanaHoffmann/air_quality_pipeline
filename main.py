from extract import fetch_data
from transform import transform_data
from load import create_table, load_data
from utils import setup_logging

logger = setup_logging()

def run_etl():
    logger.info("Iniciando pipeline ETL...")
    create_table()  # Garante que a tabela existe
    raw_data = fetch_data()
    df = transform_data(raw_data)
    load_data(df)
    logger.info("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    run_etl()
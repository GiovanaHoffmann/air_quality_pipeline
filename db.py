import os
import psycopg2
from utils import setup_logging, load_environment

logger = setup_logging()
load_environment()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST", "db"),  #'db' como fallback para Docker. Pode sobrescrever via .env
            port=os.getenv("DB_PORT")
        )
        logger.info(f"Conectado ao {os.getenv('DB_NAME')} em {os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}")
        logger.info(f"Usuário: {os.getenv('DB_USER')}")
        return conn
    except psycopg2.Error as e:
        logger.error(f"Erro de conexão: {e}")
        return None
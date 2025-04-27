import logging
from dotenv import load_dotenv
import os  

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

def load_environment():
    load_dotenv()
    # Valida variáveis obrigatórias
    REQUIRED_ENV_VARS = ["DB_NAME", "DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "API_KEY"]
    for var in REQUIRED_ENV_VARS:
        if not os.getenv(var):
            raise EnvironmentError(f"Variável de ambiente {var} não definida.")
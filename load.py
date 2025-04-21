from db import get_db_connection
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def create_table():
    conn = get_db_connection()
    if not conn:
        return

    cur = conn.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS air_quality (
                id SERIAL PRIMARY KEY,
                city VARCHAR(255),
                latitude FLOAT,
                longitude FLOAT,
                date DATE,  -- coluna separada para data
                time TIME,  -- coluna separada para hora
                date_time_unix BIGINT,  -- timestamp original
                air_quality_index INT,
                carbon_monoxide FLOAT,
                nitrogen_monoxide FLOAT,
                nitrogen_dioxide FLOAT,
                ozone FLOAT,
                sulphur_dioxide FLOAT,
                fine_particles FLOAT,
                coarse_particles FLOAT,
                ammonia FLOAT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_timestamp ON air_quality (timestamp);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_date ON air_quality (date);")  # Índice para data
        conn.commit()
        logging.info("Tabela criada ou verificada com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao criar tabela: {e}")
    finally:
        cur.close()
        conn.close()

def load_data(df):
    if df is None or df.empty:
        logging.warning("Nenhum dado para inserir.")
        return

    conn = get_db_connection()
    if not conn:
        return

    cur = conn.cursor()
    try:
        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO air_quality (
                    city, latitude, longitude, date, time, date_time_unix,
                    air_quality_index, carbon_monoxide, nitrogen_monoxide,
                    nitrogen_dioxide, ozone, sulphur_dioxide,
                    fine_particles, coarse_particles, ammonia
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (
                row["city"], row["latitude"], row["longitude"],
                row["date"], row["time"], row["date_time_unix"],
                row["air_quality_index"], row["carbon_monoxide"],
                row["nitrogen_monoxide"], row["nitrogen_dioxide"],
                row["ozone"], row["sulphur_dioxide"],
                row["fine_particles"], row["coarse_particles"],
                row["ammonia"]
            ))
        conn.commit()
        logging.info("Dados carregados com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
    finally:
        cur.close()
        conn.close()
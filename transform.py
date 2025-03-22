import pandas as pd
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def transform_data(data_list):
    if not data_list:
        logging.error("Nenhum dado para transformar.")
        return None

    records = []
    for data in data_list:
        if not data or "list" not in data:
            logging.error(f"Dados incompletos para {data.get('city', 'cidade desconhecida')}.")
            continue

        for entry in data["list"]:
            record = {
                "city": data["city"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
                "date_time": entry["dt"],
                "air_quality_index": entry["main"]["aqi"],
                "carbon_monoxide": entry["components"]["co"],
                "nitrogen_monoxide": entry["components"]["no"],
                "nitrogen_dioxide": entry["components"]["no2"],
                "ozone": entry["components"]["o3"],
                "sulphur_dioxide": entry["components"]["so2"],
                "fine_particles": entry["components"]["pm2_5"],
                "coarse_particles": entry["components"]["pm10"],
                "ammonia": entry["components"]["nh3"],
            }
            records.append(record)

    logging.info("Dados transformados com sucesso.")
    return pd.DataFrame(records)
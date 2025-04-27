import pandas as pd
from utils import setup_logging
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

logger = setup_logging()

def transform_data(data_list, local_timezone='America/Sao_Paulo'):
    if not data_list:
        logger .error("Nenhum dado para transformar.")
        return None

    # Configura o timezone local
    local_tz = ZoneInfo(local_timezone)

    records = []
    for data in data_list:
        if not data or "list" not in data:
            logger.error(f"Dados incompletos para {data.get('city', 'cidade desconhecida')}")
            continue

        for entry in data["list"]:
            # Converte timestamp Unix para datetime com timezone UTC
            dt_utc = datetime.fromtimestamp(entry["dt"], tz=timezone.utc)
            
            # Converte para o timezone local
            dt_local = dt_utc.astimezone(local_tz)
            
            # Extrai data e hora formatadas
            date_str = dt_local.strftime('%Y-%m-%d')
            time_str = dt_local.strftime('%H:%M:%S')
            
            record = {
                "city": data["city"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
                "date": date_str,
                "time": time_str,
                "timezone": str(local_tz),  # armazena o timezone usado
                "date_time_unix": entry["dt"],
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

    logger.info("Dados transformados com sucesso.")
    return pd.DataFrame(records)
import os
import requests
from dotenv import load_dotenv
import logging

load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY = os.getenv("API_KEY")

# Coordenadas das capitais brasileiras (latitude, longitude)
CAPITALS = {
    "Rio Branco": (-9.9747, -67.8100),
    "Maceió": (-9.6658, -35.7353),
    "Macapá": (0.0349, -51.0664),
    "Manaus": (-3.1190, -60.0217),
    "Salvador": (-12.9711, -38.5108),
    "Fortaleza": (-3.7319, -38.5267),
    "Brasília": (-15.7801, -47.9292),
    "Vitória": (-20.3194, -40.3378),
    "Goiânia": (-16.6869, -49.2648),
    "São Luís": (-2.5387, -44.2823),
    "Cuiabá": (-15.6010, -56.0974),
    "Campo Grande": (-20.4697, -54.6201),
    "Belo Horizonte": (-19.9167, -43.9345),
    "Belém": (-1.4558, -48.4902),
    "João Pessoa": (-7.1195, -34.8450),
    "Curitiba": (-25.4296, -49.2713),
    "Recife": (-8.0543, -34.8813),
    "Teresina": (-5.0892, -42.8016),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Natal": (-5.7793, -35.2009),
    "Porto Alegre": (-30.0331, -51.2300),
    "Porto Velho": (-8.7612, -63.9005),
    "Boa Vista": (2.8195, -60.6714),
    "Florianópolis": (-27.5969, -48.5495),
    "São Paulo": (-23.5505, -46.6333),
    "Aracaju": (-10.9472, -37.0731),
    "Palmas": (-10.2491, -48.3243),
}          

def fetch_data():
    all_data = []
    for city, (lat, lon) in CAPITALS.items():
        URL = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        try:
            response = requests.get(URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            data["city"] = city  # Adiciona o nome da cidade ao JSON
            all_data.append(data)
            logging.info(f"Dados para {city} extraídos com sucesso.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao obter dados para {city}: {e}")
    return all_data
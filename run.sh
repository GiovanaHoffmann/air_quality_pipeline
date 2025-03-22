#!/bin/bash

# Iniciar o banco de dados e o Airflow
docker-compose up -d

# Inicializar o Airflow
airflow db init
airflow webserver -p 8080 &
airflow scheduler
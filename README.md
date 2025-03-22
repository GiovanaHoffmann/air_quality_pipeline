# **Projeto: Pipeline de Qualidade do Ar com Apache Airflow**

Este projeto é um pipeline ETL (Extract, Transform, Load) que coleta dados de qualidade do ar de todas as capitais brasileiras usando a API do OpenWeatherMap, transforma os dados e os carrega em um banco de dados PostgreSQL. O pipeline é orquestrado pelo Apache Airflow, permitindo execuções automatizadas e monitoramento.

---

## **📌 Sumário**
- [**Projeto: Pipeline de Qualidade do Ar com Apache Airflow**](#projeto-pipeline-de-qualidade-do-ar-com-apache-airflow)
  - [**📌 Sumário**](#-sumário)
  - [**🌐 Visão Geral**](#-visão-geral)
  - [**🚀 Funcionalidades**](#-funcionalidades)
  - [**🛠 Tecnologias Utilizadas**](#-tecnologias-utilizadas)
  - [**📂 Estrutura do Projeto**](#-estrutura-do-projeto)
  - [**📋 Pré-requisitos**](#-pré-requisitos)
  - [**⚙ Configuração do Ambiente**](#-configuração-do-ambiente)
  - [**▶ Executando o Projeto**](#-executando-o-projeto)
  - [**📄 Explicação dos Arquivos**](#-explicação-dos-arquivos)
  - [**📞 Contato**](#-contato)

---

## **🌐 Visão Geral**
O projeto tem como objetivo monitorar a qualidade do ar em todas as capitais brasileiras. Ele coleta dados da API do OpenWeatherMap, transforma esses dados em um formato adequado e os armazena em um banco de dados PostgreSQL. O Apache Airflow é usado para orquestrar o pipeline, permitindo execuções automatizadas e monitoramento.

---

## **🚀 Funcionalidades**
- **Extração de Dados**: Coleta dados de qualidade do ar de todas as capitais brasileiras.
- **Transformação de Dados**: Converte os dados brutos em um formato estruturado.
- **Carga de Dados**: Armazena os dados transformados em um banco de dados PostgreSQL.
- **Orquestração**: Usa o Apache Airflow para agendar e monitorar o pipeline.
- **Logging**: Registra mensagens de log para facilitar a depuração e o monitoramento.

---

## **🛠 Tecnologias Utilizadas**
- **Python**: Linguagem de programação principal.
- **Apache Airflow**: Orquestração do pipeline.
- **PostgreSQL**: Armazenamento dos dados.
- **Docker**: Contêinerização do banco de dados e do Airflow.
- **API do OpenWeatherMap**: Fonte dos dados de qualidade do ar.
- **Pandas**: Manipulação de dados.
- **Psycopg2**: Conexão com o PostgreSQL.
- **Requests**: Requisições HTTP para a API.

---

## **📂 Estrutura do Projeto**
```
air_quality_pipeline/
│── .env                  # Variáveis de ambiente
│── .gitignore            # Arquivos e diretórios ignorados pelo Git
│── docker-compose.yml    # Configuração do PostgreSQL e Airflow
│── requirements.txt      # Dependências do projeto
│── README.md             # Documentação do projeto
│── main.py               # Script principal do pipeline
│── extraction.py         # Extração de dados da API
│── transform.py          # Transformação dos dados
│── load.py               # Carga dos dados no PostgreSQL
│── db.py                 # Conexão com o PostgreSQL
│── logs/                 # Arquivos de log
│── airflow/
│   └── dags/
│       └── etl.py        # DAG do Apache Airflow
```

---

## **📋 Pré-requisitos**
- **Docker**: Para rodar o PostgreSQL e o Apache Airflow.
- **Python 3.8+**: Para executar o pipeline.
- **Conta no OpenWeatherMap**: Para obter uma chave de API.

---

## **⚙ Configuração do Ambiente**
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/air_quality_pipeline.git
   cd air_quality_pipeline
   ```

2. **Crie um arquivo `.env`**:
   - Renomeie o arquivo `.env.example` para `.env`.
   - Adicione sua chave de API do OpenWeatherMap e as credenciais do banco de dados.

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o PostgreSQL e o Airflow**:
   ```bash
   docker-compose up -d
   ```

---

## **▶ Executando o Projeto**
1. **Execute o pipeline manualmente**:
   ```bash
   python main.py
   ```

2. **Acesse o Apache Airflow**:
   - Abra o navegador e acesse [http://localhost:8080](http://localhost:8080).
   - A DAG `air_quality_etl` estará disponível para execução.

3. **Verifique os logs**:
   - Os logs são armazenados na pasta `logs/`.

---

## **📄 Explicação dos Arquivos**
- **`.env`**: Armazena variáveis de ambiente, como chave de API e credenciais do banco de dados.
- **`docker-compose.yml`**: Configura o PostgreSQL e o Apache Airflow em contêineres Docker.
- **`main.py`**: Script principal que executa o pipeline ETL.
- **`extract.py`**: Extrai dados da API do OpenWeatherMap.
- **`transform.py`**: Transforma os dados brutos em um formato estruturado.
- **`load.py`**: Carrega os dados transformados no PostgreSQL.
- **`db.py`**: Gerencia a conexão com o banco de dados.
- **`airflow/dags/etl.py`**: Define a DAG do Apache Airflow para orquestrar o pipeline.

---

## **📞 Contato**
- **Linkedin**: [Giovana Hoffmann](www.linkedin.com/in/giovana-hoffmann-a53987255)


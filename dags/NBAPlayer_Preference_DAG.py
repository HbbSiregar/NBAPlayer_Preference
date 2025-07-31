'''
=================================================
Name  : Ma'ruf Habibie Siregar

This program is created to automate loading, transforming, and pushing data from PostgreSQL to Elasticsearch.  
The dataset used is NBA player statistics up to the 2021/2022 season.
=================================================
'''
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2
import os
from elasticsearch import Elasticsearch, helpers

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Data fetching function
def fetch_data(**kwargs):
    '''This function fetches data from PostgreSQL with user: airflow'''
    conn = psycopg2.connect(
        host='postgres', 
        port=5432,
        database='m3',
        user='airflow',
        password='airflow'
    )
    query = "SELECT * FROM public.nba_player_data_raw"
    df = pd.read_sql(query, conn)
    conn.close()
    kwargs['ti'].xcom_push(key='raw_data', value=df.to_json())
    print("Data successfully fetched from PostgreSQL")

# Data preprocessing function (cleaning + save to csv)
def data_preprocessing_all(**kwargs): 
    '''This function cleans, normalizes data, and saves the result to CSV'''
    ti = kwargs['ti']
    json_str = ti.xcom_pull(key='raw_data', task_ids='fetch_data_task')
    df = pd.read_json(json_str)

    # Data cleaning
    df = df.drop_duplicates()
    print(f'Number of records after removing duplicates: {len(df)}')

    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    print(f'Number of missing values before filling: {df.isna().sum().sum()}')
    df = df.fillna(0)
    print(f'Number of missing values after filling: {df.isna().sum().sum()}')

    if 'year' in df.columns:
        df['year_start'] = df['year'].str.split('-').str[0].astype(int)
        df['year_end'] = df['year'].str.split('-').str[1].astype(int) 

    if 'pos' in df.columns:
        df['main_pose'] = df['pos'].str.split('-').str[0]
        print("The 'main_pose' column was successfully created with the main position from the 'pos' column")

    df['ID'] = df['player'] + "_" + df['tm'] + "_" + df['year']
    print("Unique ID column successfully created by combining player, team, and year")

    # Save to CSV within this function
    output_dir = "/opt/airflow/Data_Clean"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "NBAPlayer_Preference_data_clean.csv")
    df.to_csv(output_path, index=False)
    print(f"Cleaned data successfully saved to {output_path}")

    ti.xcom_push(key='cleaned_data_path', value=output_path)

# Push data to Elasticsearch function
def post_to_elasticsearch(**kwargs):
    '''This function reads the cleaned CSV file and inserts it into Elasticsearch'''
    ti = kwargs['ti']
    csv_path = ti.xcom_pull(key='cleaned_data_path', task_ids='data_preprocessing_task')

    es = Elasticsearch(hosts=["http://elasticsearch:9200"])
    if not es.ping():
        raise ValueError("Failed to connect to Elasticsearch")

    df = pd.read_csv(csv_path)

    actions = [
        {
            "_index": "nba_player_clean_data",
            "_id": row['ID'],
            "_source": row.dropna().to_dict()
        }
        for _, row in df.iterrows()
    ]

    helpers.bulk(es, actions)
    print(f"{len(actions)} records successfully inserted into Elasticsearch")

with DAG(
    "NBAPlayer_Preference_DAG",
    schedule_interval="10,20,30 9 * * 6",
    catchup=False,
    default_args=default_args,
) as dag:

    fetch_data_task = PythonOperator(
        task_id='fetch_data_task',
        python_callable=fetch_data
    )

    data_preprocessing_task = PythonOperator(
        task_id='data_preprocessing_task',
        python_callable=data_preprocessing_all
    )

    post_to_es_task = PythonOperator(
        task_id='post_to_elasticsearch_task',
        python_callable=post_to_elasticsearch
    )

    fetch_data_task >> data_preprocessing_task >> post_to_es_task

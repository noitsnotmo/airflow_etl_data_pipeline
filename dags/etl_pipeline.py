
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

# Original PostgresOperator is deprecated, so we use the new one:
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime, timedelta

# Import the function we created in the previous step (extract.py)
from extract import extract_data



with DAG(
  'etl_twitter_pipeline',
  description="A simple twitter ETL pipeline using Python,PostgreSQL and Apache Airflow",
  start_date=datetime(year=2023, month=2, day=5),
  schedule_interval=timedelta(minutes=5)
) as dag:
  
  start_pipeline = EmptyOperator(
		task_id='start_pipeline',
	)
  
  create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres_connection',
    sql='sql/create_table.sql'
  )
  
  
  etl = PythonOperator(
    task_id = 'extract_data',
    python_callable = extract_data
  )

  
  clean_table = PostgresOperator(
      task_id='clean_sql_table',
      postgres_conn_id='postgres_connection',
      sql=["""TRUNCATE TABLE twitter_etl_table"""]
  )
    
  end_pipeline = EmptyOperator(
      task_id='end_pipeline',
  )

  start_pipeline >> create_table >> etl >> clean_table >> end_pipeline
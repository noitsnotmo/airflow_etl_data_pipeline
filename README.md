# airflow_etl_data_pipeline

I followed along with the article "How to Orchestrate an ETL Data Pipeline with Apache Airflow" from FreeCodeCamp.org found here:
https://www.freecodecamp.org/news/orchestrate-an-etl-data-pipeline-with-apache-airflow/

# Skills Practiced:
- Data extraction (from Twitter)
- Reading documentation to aid in debugging
- Python and SQL coding
- Troubleshooting (macro) and debugging (micro)

# What I Learned:
- Use of Airflow operators
- How to write a DAG script in Python
- How to load data into a database
- How to connect Postgres to Airflow UI
- What a configuration (.cfg) file is and how to use it
- Familiarity with Airflow UI

# Changes to airflow.cfg:
- sql_alchemy_conn = postgresql+psycopg2://user:password@hostname/database_name
  - Defined postgresql connection instead of default SQL database.
- executor = LocalExecutor
  - From 'SequentialExecutor'
- load_examples = False
  - Disabled example DAGS.

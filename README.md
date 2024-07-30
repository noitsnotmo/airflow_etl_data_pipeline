# ETL Data Pipeline with Apache Airflow  
  
# Project Overview  
  
This repository demonstrates the orchestration of an ETL (Extract, Transform, Load) data pipeline using Apache Airflow, as outlined in the FreeCodeCamp.org article "How to Orchestrate an ETL Data Pipeline with Apache Airflow." The project involves automating the extraction, transformation, and loading of data, specifically from Twitter, and showcases proficiency in data engineering, Python and SQL coding, and troubleshooting.  
  
# Skills Practiced  
- Data Extraction: Extracted data from Twitter using APIs and integrated it into the pipeline.  
- Python and SQL Coding: Developed ETL scripts in Python and managed data interactions using SQL.  
- Troubleshooting and Debugging: Applied macro and micro debugging techniques to ensure robust and error-free pipeline execution.  
- Reading Documentation: Utilized documentation to aid in debugging and optimizing the pipeline.  
  
# What I Learned  
- Airflow Operators: Gained hands-on experience with various Airflow operators and their applications in managing ETL workflows.  
- Writing DAG Scripts: Learned how to write and configure Directed Acyclic Graph (DAG) scripts in Python to define and manage workflows.  
- Database Loading: Implemented data loading procedures to efficiently transfer transformed data into a PostgreSQL database.  
- Postgres and Airflow Integration: Connected PostgreSQL to the Airflow UI for seamless database interactions and monitoring.  
- Configuration Files: Understood the role and usage of configuration (.cfg) files in managing Airflow settings.  
- Airflow UI Familiarity: Became familiar with the Airflow UI for monitoring and managing ETL processes.
   
# Tools and Technologies  
- Apache Airflow: For orchestrating and scheduling ETL workflows.  
- Python: For writing DAG scripts and data transformation tasks.  
- PostgreSQL: As the target database for storing and managing data.  
- Twitter API: For data extraction.  
  
# Methodology  
1. Data Extraction:  
- Configured Airflow tasks to extract data from Twitter using the Twitter API.  
- Implemented automated scheduling for regular data extraction.  
2. Data Transformation:  
- Developed Python & SQL scripts to clean and transform data for loading.  
- Applied data validation to ensure quality and accuracy.  
3. Data Loading:  
- Created tasks to load the transformed data into PostgreSQL.  
- Managed database connections and ensured successful data insertion.  
4. Workflow Management:  
- Designed and implemented dynamic DAGs in Airflow to orchestrate the ETL pipeline.  
- Configured and monitored workflows through the Airflow UI.  
  
# Results  
- Automated Data Pipeline: Successfully automated the ETL pipeline, reducing manual effort and improving data processing efficiency.  
- Enhanced Debugging Skills: Developed strong troubleshooting and debugging skills through hands-on experience with Airflow and data pipelines.
  
# Future Work  
- Pipeline Optimization: Explore additional Airflow features and optimization techniques for enhanced pipeline performance.  
- Data Source Expansion: Integrate additional data sources to broaden the scope of the pipeline.  
  
# Changes to airflow.cfg:
- sql_alchemy_conn = postgresql+psycopg2://user:password@hostname/database_name  
- Defined postgresql connection instead of default SQL database.  
- executor = LocalExecutor  
- From 'SequentialExecutor'  
- load_examples = False  
- Disabled example DAGS.


''' Original code from tutorial: 
      sql="""CREATE TABLE IF NOT EXISTS twitter_etl_table(
      id SERIAL PRIMARY KEY,
      datetime DATE NOT NULL,
      username VARCHAR(200) NOT NULL,
      text TEXT,
      source VARCHAR(200),
      location VARCHAR(200)
    );"""
'''

# Apache Airflow log yielded error: ' psycopg2.errors.SyntaxError: syntax error at or near 	"sql" '
# The original code was not working for me and I had to remove the 'sql="""' and '"""' to make it work

-- create table twitter_etl_table
CREATE TABLE IF NOT EXISTS twitter_etl_table(
      id SERIAL PRIMARY KEY,
      datetime DATE NOT NULL,
      username VARCHAR(200) NOT NULL,
      text TEXT,
      source VARCHAR(200),
      location VARCHAR(200)
    );
import psycopg2
from sqlalchemy import inspect
import pandas as pd
from pandas import DataFrame

class RepositoryBase:
    
    def __init__(self, connection, engine: str, schema: str, tableName):
        
        self.dbname = 'postgres'
        self.connection = connection
        self.cursor = connection.cursor()

        self.engine = engine
        self.schema = schema
        self.tableName = tableName

    def salvaDatabase(self, lst: list):

        df: DataFrame = pd.DataFrame([objeto.__dict__ for objeto in lst])

        inspector = inspect(self.engine)
        table_columns = inspector.get_columns(self.tableName, schema=self.schema)

        # cria um dicionário que mapeia os tipos de dados para cada coluna
        column_types = {col['name']: col['type'] for col in table_columns}

        try:
            df.to_sql(self.tableName, con=self.engine, schema=self.schema, if_exists='replace', index=False, dtype=column_types)


        except Exception as e:
            print('\nErro ao executar script SQL - Repositório')
            print(f'\n\n Erro: {e}')
            raise e
    
    def run_query(self, query: str):
        
        self.cursor = self.connection.cursor()
        try: 
            return pd.read_sql_query(query, self.connection)
        
        except:
            print('\nErro ao executar script SQL - Controller')
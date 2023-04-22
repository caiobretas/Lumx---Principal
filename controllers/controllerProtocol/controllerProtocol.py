import psycopg2

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import pandas as pd

class ControllerProtocol:
    def __init__(self, connection):

        self.dbname = 'postgres'
        self.connection = connection
        self.cursor = None
    
    def __str__(self) -> str:
        return f'\nConexão ao {self.dbname.capitalize()} bem sucedida\n'
    
    def __repr__(self) -> str:
        return f'\nConexão ao {self.dbname.capitalize()} bem sucedida\n'

    def run_query(self, query: str):
        
        self.cursor = self.connection.cursor()
        try: 
            return pd.read_sql_query(query, self.connection)
        
        except:
            print('\nErro ao executar script SQL - Controller')
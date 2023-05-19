import psycopg2
from sqlalchemy import inspect
import pandas as pd
from pandas import DataFrame

class RepositoryBase:
    
    def __init__(self, connection, engine: str, schema: str, tableName):
        self.path = 'interface.xlsx' # excel
        self.dbname = 'postgres'
        
        self.connection: psycopg2.connection = connection
        self.cursor = self.connection.cursor()

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
            
            
    def openDataFrame(self) -> pd.DataFrame: # excel
        try:
            return pd.read_excel(
            io=self.path,
            sheet_name=self.tableName,
            header=0
        )
        except:
            raise Exception
    
    def salvaInterface(self, lst: list):
        with pd.ExcelWriter(path=self.path, mode='a', if_sheet_exists='overlay') as writer:
            try:
                dataFrame: DataFrame = pd.DataFrame([vars(obj) for obj in lst])
                
                dataFrame.to_excel(
                    writer, 
                    sheet_name=self.worksheetName, 
                    index=False,
                    engine='openpyxl',
                    # float_format="%.2f",
                )
            except Exception as ex:
                print("Houve um erro ao salvar dados na Interface. \n{}".format(ex))

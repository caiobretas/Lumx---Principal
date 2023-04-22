from pandas import DataFrame
from .controllerFinance import ControllerFinance

class ControllerVolume(ControllerFinance):
    def __init__(self, connection):
        self.dbname = 'postgres'
        self.connection = connection
        self.cursor = None
    
    def __str__(self) -> str:
        return f'\nConexão ao {self.dbname.capitalize()} bem sucedida\n'
    
    def __repr__(self) -> str:
        return f'\nConexão ao {self.dbname.capitalize()} bem sucedida\n'
    
    def getVolume(self, type):

        query = """
"""
        df: DataFrame = self.run_query(query=query)
        return self.run_query(query=query)
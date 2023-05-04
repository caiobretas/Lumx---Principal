import psycopg2
from time import time
from sqlalchemy import create_engine
from datetime import datetime

from business.atualizaRepository import AtualizaFinanceRepository
from business.updateProjection import UpdateProjection

class Main:
    def __init__(self) -> None:
        
        print('\nProgram starting')
        self.start_time = time()
        self.today = datetime.now().date()
        self.pathDB = 'database.xlsx'
        self.pathIF = 'interface.xlsx'
        self.pathVW = 'viewer.xlsx'
        self.pathProjection = 'projection.xlsx'
        
        self.hostProtocol = 'protocol-prod.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.portProtocol = '5432'

        self.userProtocol = 'financeiro'
        self.passwordProtocol = 'F1n@nceiro2502'
        self.dbnameProtocol = 'postgres'

        self.host= 'financeiro.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.port = '5432'
        self.user = 'postgres'
        self.password = 'financeiro2502lumx..'
        self.dbname = 'postgres'
        self.schema = 'finance'
        self.connectionProtocol = psycopg2.connect(host=self.hostProtocol, port=self.portProtocol, dbname=self.dbnameProtocol, user=self.userProtocol, password=self.passwordProtocol)
        self.connection = psycopg2.connect(host=self.host, port=self.port, dbname= self.dbname, user=self.user, password=self.password)
        self.engineAdmin = create_engine(f'postgresql://{self.user}:{self.password}@{self.host}/{self.dbname}')

    def finance(self):
        # from business.updateFiatTransactions import UpdateFiatTransactions
        # from business.postTransaction import PostTransaction
        
        # AtualizaFinanceRepository(connFinance=self.connection, engine=self.engineAdmin, schema=self.schema, pathIF=self.pathIF,connProtocol=self.connectionProtocol)
        UpdateProjection(pathProjection=self.pathProjection, connProtocol=self.connectionProtocol, connFinance=self.connection, engineAdmin=self.engineAdmin, schema=self.schema)
        
    def hr(self):
        self.schemaHR = 'h_resources'

        from business.updateContacts import UpdateContacts
        UpdateContacts(connection=self.connection, engine=self.engineAdmin, schema=self.schemaHR, tableName='contacts')
    
    def rotine(self):

        self.finance()

        print('\nRotine in {:.2f} seconds\n'.format(time() - self.start_time))


    # def test(self):

Main().rotine()
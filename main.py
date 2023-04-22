import psycopg2
from time import time
from sqlalchemy import create_engine

from business.atualizaRepository import AtualizaFinanceRepository
from business.atualizaViewer import AtualizaViewer

class Main:
    def __init__(self) -> None:
        print('\nProgram starting')
        self.start_time = time()

        self.pathDB = 'database.xlsx'
        self.pathIF = 'interface.xlsx'
        self.pathVW = 'viewer.xlsx'
        

        self.hostProtocol = 'protocol-prod.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.portProtocol = '5432'
        self.userProtocol = 'financeiro'
        self.passwordProtocol = 'F1n@nceiro2502'
        self.dbnameProtocol = 'postgres'

        self.hostFinance = 'financeiro.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.portFinance = '5432'
        self.userFinance = 'postgres'
        self.passwordFinance = 'financeiro2502lumx..'
        self.dbnameFinance = 'postgres'
        self.schemaFinance = 'finance'
        
        self.engineAdmin = create_engine(f'postgresql://{self.userFinance}:{self.passwordFinance}@{self.hostFinance}/{self.dbnameFinance}')

        self.connectionProtocol = psycopg2.connect(host=self.hostProtocol, port=self.portProtocol, dbname=self.dbnameProtocol, user=self.userProtocol, password=self.passwordProtocol)
        self.connectionFinance = psycopg2.connect(host=self.hostFinance, port=self.portFinance, dbname=self.dbnameFinance, user=self.userFinance, password=self.passwordFinance)
        
    def Finance(self):

        # from business.updateFiatTransactions import UpdateFiatTransactions
        # from business.postTransaction import PostTransaction

        AtualizaFinanceRepository(connFinance=self.connectionFinance, engine=self.engineAdmin, schema=self.schemaFinance, pathIF=self.pathIF,connProtocol=self.connectionProtocol)
        # AtualizaViewer(pathVW=self.pathVW, pathIF=self.pathIF, connProtocol=self.connectionProtocol, connFinance=self.connectionFinance, engineAdmin=self.engineAdmin, schema=self.schemaFinance)

    # def HumanResources(self):
    
    def rotina(self):

        self.Finance()

        print('\nRotine in {:.2f} seconds\n'.format(time() - self.start_time))

Main().rotina()

# import schedule
# from time import sleep
    
# schedule.every(1).minutes.do(Main().rotina)

# while True:
#     schedule.run_pending()
#     sleep(1)

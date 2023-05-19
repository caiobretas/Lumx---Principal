import psycopg2
import json
from time import time
from sqlalchemy import create_engine
from datetime import datetime

from business.atualizaRepository import UpdateFinanceRepository
from business.updateProjection import UpdateProjection

from time import time
from datetime import datetime

class Main:
    def __init__(self):
        print('\nProgram starting')
        self.start_time = time()
        self.today = datetime.now().date()
        
        self.hostProtocol = 'protocol-prod.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.portProtocol = '5432'
        self.userProtocol = 'financeiro'
        self.passwordProtocol = 'F1n@nceiro2502'
        self.dbnameProtocol = 'postgres'
        
        self.host = 'financeiro.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.port = '5432'
        self.user = 'postgres'
        self.password = 'financeiro2502lumx..'
        self.dbname = 'postgres'
        self.schema = 'finance'
        
        self.connectionProtocol = psycopg2.connect(
            host=self.hostProtocol,
            port=self.portProtocol,
            dbname=self.dbnameProtocol,
            user=self.userProtocol,
            password=self.passwordProtocol
        )
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        self.engineAdmin = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}/{self.dbname}'
        )

    def finance(self):
        UpdateFinanceRepository(self.connection,self.engineAdmin)
        UpdateProjection(self.connection,self.engineAdmin)
        
    # def hr(self):
    #     self.schemaHR = 'h_resources'
    #     from business.updateContacts import UpdateContacts
    #     UpdateContacts(connection=self.connection, engine=self.engineAdmin, schema=self.schemaHR, tableName='contacts')
    
    def routine(self):
        self.finance()
        print('\nRoutine in {:.2f} seconds\n'.format(time() - self.start_time))

Main().routine()

from controllers.controllerHTTP.controllerKamino import ControllerKamino
list_transactions = ControllerKamino().getTransactions()
print(list_transactions)
# from controllers.controllerHTTP.controllerGoogle import GoogleGmail

# gmail = GoogleGmail()
# gmail.setMessage()
# # GoogleGmail().getEmails()
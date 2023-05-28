import psycopg2
from time import time
from sqlalchemy import create_engine
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
        self.engine = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}/{self.dbname}'
        )
    
    def emailrequests(self):
        from business.evaluateInvoiceRequest import EvaluateInvoiceRequest
        EvaluateInvoiceRequest(self.connection, self.engine).createInvoiceRequest() # send the Invoice Request by e-mail
    
    def flows(self):
        from business.financeControl import Flow
        Flow(self.connection, self.engine).salaryFlow()
        
    def admin(self):
        from business.updateEmailRequests import UpdateEmailRequests
        UpdateEmailRequests(self.connection, self.engine).updateEmailRequests()
        
    def finance(self):
        from business.atualizaRepository import UpdateFinanceRepository
        from business.updateProjection import UpdateProjection
        UpdateFinanceRepository(self.connection,self.engine)
        UpdateProjection(self.connection,self.engine)
        
    def hr(self):
        from business.updateContacts import UpdateContacts
        UpdateContacts(connection=self.connection, engine=self.engine)
    
    def routine(self):
        self.hr()
        self.finance()
        self.admin()
        self.flows()
        
        print('\nRoutine in {:.2f} seconds\n'.format(time() - self.start_time))
        
# Main().routine()
Main().emailrequests()
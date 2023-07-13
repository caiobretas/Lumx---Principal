import psycopg2
from time import time
from sqlalchemy import create_engine
from datetime import datetime

from business.comercial import PipedriveDealFields

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
        
        self.host = 'financeiro-15.czhdzceztpsv.us-east-1.rds.amazonaws.com'
        self.port = '5432'
        self.user = 'postgres'
        self.password = 'F1nanc&1ro2502'
        self.dbname = 'postgres'
        self.schema = 'finance'
        
        self.engineProtocol = create_engine(f'postgresql://{self.userProtocol}:{self.passwordProtocol}@{self.hostProtocol}/{self.dbnameProtocol}')
        
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
        EvaluateInvoiceRequest(self.connection, self.engine).sendInvoiceRequest() # send the Invoice Request
        EvaluateInvoiceRequest(self.connection, self.engine).sendInvoiceReminder() # send the Invoice Reminder, if needed.
    
    def flows(self):
        from business.finance.FinanceControl_sheet import FinanceControl
        from business.financeControl import Flow
        
        FinanceControl(self.connection,self.engine,self.connectionProtocol, self.engineProtocol).updateSheet()
        Flow(self.connection, self.engine).salaryFlow()
    
    def legal(self):
        from business.legal.legalControl_sheet import LegalControlSheet
        from business.legal.documentsRepository import DocumentsRepository
        from business.legal.updateLegalRepository import UpdateLegalRepository

        DocumentsRepository(self.connection, self.engine).update()
        UpdateLegalRepository(self.connection, self.engine).update()
        LegalControlSheet(self.connection,self.engine).routine()
    
    def comercial(self):
        from business.comercial import PipedriveDeals, PipedriveActivities,PipedriveDealFields
        
        PipedriveDeals.PipedriveDeals(self.connection,self.engine).update()
        # PipedriveDeals.PipedriveDeals(self.connection,self.engine).getFlow()
        PipedriveActivities.PipedriveActivities(self.connection,self.engine).update()
        PipedriveDealFields.PipedriveDealField(self.connection,self.engine).update()
    
    def admin(self):
        from business.updateEmailRequests import UpdateEmailRequests
        UpdateEmailRequests(self.connection, self.engine).update()
        
    def finance(self):
        from repositories.protocol.repositoryWallets import RepositoryWallets
        from business.finance.updateProjects import UpdateProjects
        from business.atualizaRepository import FinanceRepository
        from business.updateProjection import UpdateProjection
        from business.finance.ExchangeVariationRate import ExchangeVariationRate
        
        UpdateProjects(self.connection,self.engine).update()
        ExchangeVariationRate(self.connection,self.engine).updateSheet()
        FinanceRepository(self.connection,self.engine).update()
        UpdateProjection(self.connection,self.engine).update()
        
    def hr(self):
        from business.updateContacts import UpdateContacts
        UpdateContacts(connection=self.connection, engine=self.engine).update()
    
    def routine(self):
        
        self.hr()
        self.admin()
        self.finance()
        self.flows()
    
        print('\nRoutine in {:.2f} seconds\n'.format(time() - self.start_time))
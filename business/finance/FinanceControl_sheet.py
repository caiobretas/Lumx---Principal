from repositories.protocol.repositoryWallets import RepositoryWallets
from repositories.repositoryProjects import RepositoryProjects
from repositories.repositoryContacts import RepositoryContacts
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets

class FinanceControl:
    
    def __init__(self, connection=None, engine=None, connectionProtocol=None, engineProtocol=None):
        self.repositoryWallets = RepositoryWallets(connectionProtocol, engineProtocol)
        self.repositoryProjects = RepositoryProjects(connection, engine)
        self.repositoryContacts = RepositoryContacts(connection, engine)
        self.controllerGoogleSheets = GoogleSheets()
        
        self.worksheetId = '1SYSnWnoDzDD6aU0VONx0vWfqlgAckrnhFb-uPc6xr_E'
    
    def writeProject_sheet(self):
        
        sheetId = 155755790
        headers = ['project_id','project_name','client_id','wallet','smartcontract','blockchain','ativo','statusupdatedate','currency','currencycrypto','setupfee','maintancefee','primarysalefee','secondarysalefee','pixfee','min_pixfee','creditcardfee','connect','activeuser','wallet']
        query = f"select id,project_name,client_id,client_royalties_address,contract_address,blockchain_symbol,ativo,statusupdatedate,currency,currencycrypto,setupfee,maintancefee,primarysalefee,secondarysalefee,pixfee,min_pixfee,creditcardfee,connect,activeuser,wallet from {self.repositoryProjects.schema}.{self.repositoryProjects.tableName}"
        
        projects = self.repositoryProjects.runQuery(query)
        
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
        self.controllerGoogleSheets.writemanyRows(projects)
    
    def writeContacts_sheet(self):
        
        sheetId = 793702407
        headers = ['id', 'nome', 'CNPJ','telefone','email','emailsecundario']
        query = "select id, nomefantasia as nome_lumx, cpfcnpj AS CNPJ, telefone, email, emailsecundario from h_resources.contacts as hr left join h_resources.categories as hrc on hr.idclassificacaopreferencial = hrc.idclassificacaokamino where categoria = 'Cliente';"
        
        contacts = self.repositoryContacts.runQuery(query)
        
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
        self.controllerGoogleSheets.writemanyRows(contacts)
    
    def writeActiveUsers_sheet(self):
        
        sheetId = 205724410
        headers = ['project_id','project_name','address','provider','created_at','updated_at','is_archived']
        query = f"""select c.id as project_id, c.name as project_name,address,provider,w.created_at,updated_at,is_archived from blkx.wallets as w left join blkx.users as u on u.id = w.user_id left join blkx.clients as c on c.id = u.client_id""" 
        
        contacts = self.repositoryWallets.runQuery(query)
        
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
        self.controllerGoogleSheets.writemanyRows(contacts)
        
    # def writePrimaryVolume_sheet(self):
        
    #     sheetId = 205724410
    #     headers = ['id','user_id','wallet','provider','created_at','updated_at','is_archived']
    #     query = f"""select id,user_id,address,provider,created_at,updated_at,is_archived from {self.repositoryWallets.schema}.{self.repositoryWallets.tableName}""" 
        
    #     contacts = self.repositoryWallets.runQuery(query)
        
    #     self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
    #     self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
    #     self.controllerGoogleSheets.writemanyRows(contacts)
    
    def updateSheet(self):
        self.writeProject_sheet()
        self.writeContacts_sheet()
        self.writeActiveUsers_sheet()
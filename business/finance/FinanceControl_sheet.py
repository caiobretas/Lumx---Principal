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
        headers = ['project_id','project_name','client_id','wallet','smartcontract','blockchain','ativo','statusupdatedate','currency','currencycrypto','setupfee','maintenancefee','primarysalefee (%)','secondarysalefee (%)','pixfee (%)','min_pixfee','creditcardfee','connect','activeuser','wallet']
        query = f"select id,project_name,client_id,client_royalties_address,contract_address,blockchain_symbol,ativo,statusupdatedate,currency,currencycrypto,setupfee,maintenancefee,primarysalefee,secondarysalefee,pixfee,min_pixfee,creditcardfee,connect,activeuser,wallet from {self.repositoryProjects.schema}.{self.repositoryProjects.tableName}"
        
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
        
    def writeVolumes_sheet(self):
        
        sheetId = 205724410
        headers = ['id','project_id','project_name','type','price','amount','currency','blockchain','status', 'created_at']
        query = f"""SELECT
    coalesce (l.id, m.id) AS id,
    coalesce (l.collection_id, m.collection_id) AS project_id,
		coalesce (c.name, mc.name) AS project_name,
    coalesce (cl.name, cll.name) AS client_name,
case 
    		when m.id is not null then 'Primário'
        when l.id is not null then 'Secundário'
        else null
    end as tipo,
    
    coalesce (l.price, m.price) AS price,
    coalesce (m.amount,amount) as amount,
    coalesce (mc.currency, c.currency) AS currency,
    upper (coalesce (b.symbol, bl.symbol)) AS blockchain,
    coalesce (l.status_id, m.status_id) AS status_id,
    coalesce (l.created_at, m.created_at) AS created_at
   FROM
    blkx.listings AS l
    FULL OUTER JOIN blkx.mint_requests AS m ON l.id = m.id
    LEFT JOIN blkx.collections AS c ON c.id = l.collection_id
    LEFT JOIN blkx.collections AS mc ON mc.id = m.collection_id
    LEFT JOIN blkx.clients as cl on cl.id = c.client_id
    LEFT JOIN blkx.clients  as cll on cll.id = mc.client_id
		LEFT JOIN blkx.contracts as ct on ct.id = c.contract_id
    LEFT JOIN blkx.contracts as ctt on ctt.id = mc.contract_id
    LEFT JOIN blkx.blockchains as b on b.id = ct.blockchain_id
    LEFT JOIN blkx.blockchains as bl on bl.id = ctt.blockchain_id
    where
    		l.status_id = 'success' or m.status_id = 'success'
        or
        l.status_id = 'in_queue' or m.status_id = 'in_queue'
            order by created_at desc

    ;""" 
        
        contacts = self.repositoryWallets.runQuery(query)
        
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
        self.controllerGoogleSheets.writemanyRows(contacts)
    
    def updateSheet(self):
        self.writeProject_sheet()
        self.writeContacts_sheet()
        self.writeActiveUsers_sheet()
        self.writeVolumes_sheet()
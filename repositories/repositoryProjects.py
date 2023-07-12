import logging
import string
from entities.entityProject import Project
from gspread import Worksheet
from repositories.repositoryBase import RepositoryBase
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from entities.entityClient import Client

class RepositoryProjects ( RepositoryBase ):
    def __init__(self, connection, engine: str):
        self.tableName = 'projects'
        self.schema = 'finance'
        super().__init__(connection= connection, engine=engine, schema=self.schema, tableName=self.tableName)
        
        self.controllerGoogleSheets = GoogleSheets()
        self.workSheetId = '1z5nbW3P-NFP4rr0dEED9ySDhfM4zYol0SO3i9m8GVyU'
        self.insertSheetId = 1645953958 # alterar depois
        self.lastUpdateSheetId = 994478374
        self.workSheetHeaders =[
        'id',
        'project_name',
        'client_id',
        'client_royalties_address',
        'contract_address',
        'blockchain_symbol',
        'ativo',
        'currency',
        'currencycrypto',
        'setupfee',
        'maintancefee',
        'primarysalefee',
        'secondarysalefee',
        'pixfee',
        'min_pixfee',
        'creditcardfee',
        'connect',
        'activeuser',
        'wallet'
        ]
    
    def insert(self, list_projects: list[Project]):
        if not list_projects:
            return None
        values = [t.to_tuple() for t in list_projects]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,project_name,client_id,client_royalties_address,contract_address,blockchain_symbol,ativo,currency,currencycrypto,setupfee,maintancefee,primarysalefee,secondarysalefee,pixfee,min_pixfee,creditcardfee,connect,activeuser,wallet)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO
                    UPDATE SET
                    project_name = EXCLUDED.project_name,
                    client_id = EXCLUDED.client_id,
                    client_royalties_address = EXCLUDED.client_royalties_address,
                    contract_address = EXCLUDED.contract_address,
                    blockchain_symbol = EXCLUDED.blockchain_symbol,
                    ativo = EXCLUDED.ativo,
                    currency = EXCLUDED.currency,
                    currencycrypto = EXCLUDED.currencycrypto,
                    setupfee = EXCLUDED.setupfee,
                    maintancefee = EXCLUDED.maintancefee,
                    primarysalefee = EXCLUDED.primarysalefee,
                    secondarysalefee = EXCLUDED.secondarysalefee,
                    pixfee = EXCLUDED.pixfee,
                    min_pixfee = EXCLUDED.min_pixfee,
                    creditcardfee = EXCLUDED.creditcardfee,
                    connect = EXCLUDED.connect,
                    activeuser = EXCLUDED.activeuser,
                    wallet = EXCLUDED.wallet
                    """
                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(e)
    
    def getProjects_fromSheets(self):
        sheet: Worksheet = self.controllerGoogleSheets.openSheet(self.workSheetId, self.insertSheetId)
        
        maxColumn = len(self.workSheetHeaders)
        alphabet = string.ascii_uppercase
        index = (maxColumn - 1) % 26
        letter = alphabet[index]
        self.workSheetrange = f"A:{letter}"
        
        row_list: list = sheet.get(self.workSheetrange)
        row_numbers = len(row_list) - 1
        if row_numbers == 0:
            return
        if row_list: row_list.pop(0)
        
        self.controllerGoogleSheets.eraseSheet(self.workSheetId,self.insertSheetId, self.workSheetHeaders)
        self.controllerGoogleSheets.eraseSheet(self.workSheetId,self.lastUpdateSheetId, self.workSheetHeaders)
        
        projects: list[Project] = []
        filteredRows = []
        
        for row in row_list:
            _index = row_list.index(row)
            if not row or row[0] == '':
                continue
            
            table_range = f'A{row_numbers}:{letter}{row_numbers}'
            
            if row != self.workSheetHeaders:
                
                
                # faremos uma sessão de validação dos índices
                try:
                    client_royalties_address = row[3]
                except IndexError:
                    client_royalties_address = None
                try:
                    contract_address = row[4]
                except IndexError:
                    contract_address = None
                try:
                    blockchain_symbol = row[5]
                except IndexError:
                    blockchain_symbol = None
                try:
                    ativo = row[6]
                except IndexError:
                    ativo = None
                try:
                    currency = row[7]
                except IndexError:
                    currency = None
                try:
                    currencycrypto = row[8]
                except IndexError:
                    currencycrypto = None
                try:
                    setupfee = row[9]
                except IndexError:
                    setupfee = 0
                try:
                    maintancefee = row[10]
                    maintancefee = maintancefee
                except IndexError:
                    maintancefee = 0
                try:
                    primarysalefee = row[11] if row[11] != '' else 0
                    primarysalefee = float((str(primarysalefee).split('%')[0]).replace(',', '.'))
                except IndexError:
                    primarysalefee = 0
                try:
                    secondarysalefee = row[12] if row[12] != '' else 0
                    secondarysalefee = float((str(secondarysalefee).split('%')[0]).replace(',', '.'))
                except IndexError:
                    secondarysalefee = 0
                try:
                    pixfee = row[13] if row[13] != '' else 0
                    pixfee = float((str(pixfee).split('%')[0]).replace(',', '.'))
                except IndexError:
                    pixfee = 0
                try:
                    min_pixfee = row[14] if row[14] != '' else 0 
                    min_pixfee = float((str(min_pixfee)).replace(',', '.'))
                except IndexError:
                    min_pixfee = 0
                try:
                    creditcardfee = row[15] if row[15] != '' else 0 
                    creditcardfee = float((str(creditcardfee).split('%')[0]).replace(',', '.'))
                except IndexError:
                    creditcardfee = 0
                try:
                    connect = row[16] if row[16] != '' else False
                except IndexError:
                    connect = False
                try:
                    activeuser = row[17] if row[17] != '' else False
                except IndexError:
                    activeuser = False
                try:
                    wallet = row[18] if row[18] != '' else False
                except IndexError:
                    wallet = False

                project = Project(
                id = row[0],
                project_name = row[1],
                client_id = row[2],
                client_royalties_address = client_royalties_address,
                contract_address = contract_address,
                blockchain_symbol = blockchain_symbol,
                ativo = ativo,
                # aqui entraria a coluna com a data de atualização do status, mas é o SQL que gera,
                currency = currency,
                currencycrypto = currencycrypto,
                setupfee = setupfee,
                maintancefee = maintancefee,
                primarysalefee = primarysalefee,
                secondarysalefee = secondarysalefee,
                pixfee = pixfee,
                min_pixfee = min_pixfee,
                creditcardfee = creditcardfee,
                connect = connect,
                activeuser = activeuser,
                wallet = wallet
                )
                
                if project.id:
                    projects.append(project)
                    if row not in filteredRows: filteredRows.append(row)
        
        self.controllerGoogleSheets.openSheet(self.workSheetId,self.lastUpdateSheetId)
        self.controllerGoogleSheets.writemanyRows(filteredRows)
        return projects if row_list else None
import logging
from entities.legal.entityDocument import Document
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from controllers.controllerGoogle.controllerGoogleDrive import GoogleDrive
from repositories.legal.repositoryDocuments import RepositoryDocuments

class LegalControlSheet:
    
    def __init__(self, connection, engine):
        self.worksheetId = '1nXLvpcA1EjBUWls-3R25Zn-PdMxTW7R2WdmSm_HRnAo'
        self.repositoryDocuments = RepositoryDocuments(connection,engine)
        self.controllerGoogleSheets = GoogleSheets()
        self.controllerGoogleDrive = GoogleDrive()
    
        self.cat3 = ['Contrato', 'Comodato', 'Distrato', 'Aditivo', 'Pedido', 'Notificação', 'Devolução equipamento']
        self.cat4 = ['Parceiro','Colaborador','Fornecedor','Cliente','Sócio']
    
    def writeTrashedDocuments(self):
        headers = ['']
        
        files: list[Document] = self.controllerGoogleDrive.getFilesByDriveId(self.repositoryDocuments.driveId)
        trashed_files = [file.to_tuple() for file in files if file.trashed]
        
        self.controllerGoogleSheets.eraseSheet
        
    
    def writePossibleAnswersforCategories(self):
        
        headers = ['Categoria 3','Categoria 4']
        
        self.controllerGoogleSheets.sheetId = 1874255554
        sheetId = self.controllerGoogleSheets.sheetId
        
        # da clear na sheet
        
        try:
            
            self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
        
            for i, valueCat3 in enumerate(self.cat3):            
                self.controllerGoogleSheets.writeRow([valueCat3],self.worksheetId,sheetId,table_range=f'A{i+1}') 
          
            for i, valueCat4 in enumerate(self.cat4):
                self.controllerGoogleSheets.writeRow([valueCat4],self.worksheetId,sheetId,table_range=f'B{i+1}')
    
        except Exception as e:
            logging.error(e)
            return
    
    def writeDatabaseinSheets(self):
        query = f"select d.id, name, type, TO_CHAR(createdtime, 'YYYY-MM-DD HH24:MI:SS') as createdtime, TO_CHAR(modifiedtime, 'YYYY-MM-DD HH24:MI:SS') as modifiedtime, categoria1, categoria2, categoria3, categoria4, categoria5, weblink from {self.repositoryDocuments.schema}.{self.repositoryDocuments.tableName} as d left join legal.documents_categories as dc on dc.id = d.id order by createdtime desc"
        
        headers = ['id', 'name', 'type', 'createdtime', 'modifiedtime', 'categoria1', 'categoria2', 'categoria3', 'categoria4', 'categoria5', 'weblink']
        
        sheetId = 2042539928
        
        # da clear na sheet
        try:
            filesinRepository = self.repositoryDocuments.runQuery(query)
            
            self.controllerGoogleSheets.eraseSheet(self.worksheetId,sheetId,headers)
            
            self.controllerGoogleSheets.writemanyRows(filesinRepository)
        
        except Exception as e:
            logging.error(e)
            return
        
    def routine(self):
        self.writeDatabaseinSheets()
        self.writePossibleAnswersforCategories()
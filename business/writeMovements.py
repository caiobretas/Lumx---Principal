from repositories.repositoryTransactions import RepositoryTransaction
from viewers.viewerTransactions import ViewerTransactions

class WriteTranscations:
    def __init__(self,connection,engine,schema,path,sheetName, tableName):
        
        self.repository = RepositoryTransaction(connection,engine,schema, tableName)
        self.transactions = self.repository.getTransactions()
        
        #  writes transactions in the Excel viewer
        self.viewer = ViewerTransactions(path=path, sheetName=sheetName)
        self.viewer.insertViewerMovements(lst= self.transactions)
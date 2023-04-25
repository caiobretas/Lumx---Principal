from repositories.repositoryTransactions import RepositoryTransaction

class AssembleProjection:
    def __init__(self, connection, engine, schema, tableName):
        self.repositoryTransactions = RepositoryTransaction(connection, engine, schema, tableName)
        
    def getData(self):
        self.repositoryTransactions.getTransactions()
        
from repositories.repositoryTransactions import RepositoryTransaction

class AssembleProjection:
    def __init__(self, connection, engine, schema, tableName):
        self.connection = connection
        self.engine = engine
        self.schema = schema
        self.tableName = tableName
        
    def getRegisters(self):
        list = RepositoryTransaction(self.connection, self.engine, self.schema, self.tableName).getProjection()
        print(list)
        
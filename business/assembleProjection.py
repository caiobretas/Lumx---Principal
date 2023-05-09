from repositories.repositoryTransactions import RepositoryTransaction
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from entities.entityProjection import Projection

class AssembleProjection:
    def __init__(self, connection, engine, schema, tableName):
        self.connection = connection
        self.engine = engine
        self.schema = schema
        self.tableName = tableName
        
    def getRegisters(self) -> list[Projection]:
        list_projection: list[Projection] = []
        list_projection.extend(RepositoryTransaction(self.connection, self.engine, self.schema, 'movements').getProjection())
        list_projection.extend(RepositoryCryptoTransaction(self.connection, self.engine, self.schema, 'movements_crypto').getProjection())
        return list_projection
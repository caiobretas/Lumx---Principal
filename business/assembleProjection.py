from repositories.repositoryTransactionsKamino import RepositoryKamino
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from entities.entityProjection import Projection

class AssembleProjection:
    def __init__(self, connection, engine):
        self.connection = connection
        self.engine = engine

    def getRegisters(self) -> list[Projection]:
        list_projection: list[Projection] = []
        list_projection.extend(RepositoryKamino(self.connection, self.engine).getProjection())
        list_projection.extend(RepositoryCryptoTransaction(self.connection, self.engine).getProjection())
        return list_projection
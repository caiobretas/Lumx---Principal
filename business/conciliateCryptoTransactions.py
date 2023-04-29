from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from interfaces.interfaceConciliations import InterfaceConciliations
from entities.entityConciliation import Conciliation

class ConciliateCryptoTransactions:
    def __init__(self, path_interface, connection, engine, schema, tableName):
        list_conciliations: list[Conciliation] = InterfaceConciliations(path_interface).getConciliations()
        for obj in list_conciliations:
            RepositoryCryptoTransaction(connection, engine, schema, tableName).updatebyHash(obj.hash, obj.methodid, obj.description, obj.project)
            
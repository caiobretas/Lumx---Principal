from time import time
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from interfaces.interfaceConciliations import InterfaceConciliations
from entities.entityConciliation import Conciliation

class ConciliateCryptoTransactions:
    def __init__(self, path_interface, connection, engine, schema, tableName):
        start_time = time()
        print('\nConciliating Transactions...')
        try:
            list_conciliations: list[Conciliation] = InterfaceConciliations(path_interface).getConciliations()
            for obj in list_conciliations:
                RepositoryCryptoTransaction(connection, engine, schema, tableName).updatebyHash(obj.hash, obj.methodid, obj.description)
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
            
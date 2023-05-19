from time import time
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from repositories.repositoryConciliations import RepositoryConciliations
from entities.entityConciliation import Conciliation

class ConciliateCryptoTransactions:
    def __init__(self, connection, engine):
        start_time = time()
        print('\nConciliating Transactions...')
        try:
            list_conciliations: list[Conciliation] = RepositoryConciliations(connection, engine).getConciliations_fromExcel()
            for obj in list_conciliations:
                RepositoryCryptoTransaction(connection, engine).updatebyHash(obj.hash, obj.methodid, obj.description)
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
            
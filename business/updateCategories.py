from time import time
from interfaces.interfaceCategories import InterfaceCategories
from repositories.repositoryCategories import RepositoryCategories

class UpdateCategories:
    def __init__(self, connection, engine, pathIF, schema, sheetName, tableName):
        start_time = time()
        
        print('\nUpdating Categories...')
        try:
            RepositoryCategories(
                connection=connection,
                engine=engine,
                schema=schema,
                tableName=tableName).insertCategories(list_category=InterfaceCategories(pathIF=pathIF, sheetName=sheetName).getCategories())
            status = 'Complete'
            
        except:
            status = 'Failed'
            return None
        
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
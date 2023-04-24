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
                tableName=tableName).insertCategories(lst=InterfaceCategories(pathIF=pathIF, sheetName=sheetName).getCategories())
            status = 'Complete'
            
        except Exception as e:
            status = 'Failed'
            return None
        
        finally:
            try_time = time()
            print('{} Status: {} - Time: {}'.format(status,' ' * 1,round(try_time - start_time, 3)))
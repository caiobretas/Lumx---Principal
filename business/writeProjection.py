from time import time
from entities.entityProjection import Projection
from business.assembleProjection import AssembleProjection
from viewers.viewerProjection import ViewerProjection

class WriteProjection:
    def __init__(self, path, sheetName, connection, engine, schema, tableName):
        start_time = time()
        print('\nUpdating transactions...')
        try:
            list_projection: list[Projection] = AssembleProjection(connection, engine, schema, tableName).getRegisters()
            ViewerProjection(path=path, sheetName=sheetName).insertViewerProjection(list_projection)
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
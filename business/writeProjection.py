from time import time
from entities.entityProjection import Projection
from business.assembleProjection import AssembleProjection
from viewers.viewerProjection import ViewerProjection

class WriteProjection:
    def __init__(self, path, connection, engine, schema):
        self.path = path
        self.connection = connection
        self.engine = engine
        self.schema = schema
        self.tableName = 'movements'
        
    def insert_projectionTable(self, sheetName):
        start_time = time()
        print('\nWriting database...')
        
        try:
            list_projection: list[Projection] = AssembleProjection(self.connection, self.engine, self.schema, self.tableName).getRegisters()
            ViewerProjection(path=self.path, sheetName=sheetName).insertViewerProjection(list_projection)
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
        
from time import time
from entities.entityProjection import Projection
from business.assembleProjection import AssembleProjection
from controllers.controllerHTTP.controllerGoogle import GoogleSheets
import pandas as pd
# from viewers.viewerProjection import ViewerProjection

class WriteProjection:
    def __init__(self, worksheetId, sheetName, connection, engine, schema):
        self.worksheetId = worksheetId
        self.sheetName = sheetName
        self.connection = connection
        self.engine = engine
        self.schema = schema
        self.tableName = 'movements'
        
    def writeMovements(self):
        start_time = time()
        print('\nWriting database...')
        
        try:
            list_objMovements: list[Projection] = AssembleProjection(self.connection, self.engine, self.schema, self.tableName).getRegisters()
            from business.transformObjDict import TransformObj
            list_valuesMovements = TransformObj().objects_to_values(list_objMovements)
                
            GoogleSheets().updateWorksheet_byID(worksheetId=self.worksheetId, list_values=list_valuesMovements, sheetName=self.sheetName)
            # ViewerProjection(path=self.path, sheetName=sheetName).insertViewerProjection(list_projection)
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
            
    # def writePrices(self):
        
    #     self.viewer: pd.DataFrame = ViewerPrices(path=self.path, sheetName=self.sheetName)
    #     repositoryPrices = RepositoryPrices(self.connection, self.engine, self.schema, self.tableName)
    #     start_time = time()
    #     print('\nWriting prices...')
        
    #     try:
    #         list_prices: list[Coin] = repositoryPrices.getProjection()
    #         self.viewer.insertPrices(list_obj=list_prices)
    #         status = 'Complete'
    #     except:
    #         status = 'Failed'
    #         raise Exception
    #     finally:
    #         try_time = time()
    #         print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
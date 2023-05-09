import logging
from time import time
from entities.entityProjection import Projection, Projection_Price
from business.transformObjDict import TransformObj
from business.assembleProjection import AssembleProjection
from repositories.repositoryPrices import RepositoryPrices
from controllers.controllerHTTP.controllerGoogle import GoogleSheets
import pandas as pd
# from viewers.viewerProjection import ViewerProjection

class WriteProjection:
    def __init__(self, worksheetId, connection, engine, schema):
        
        self.worksheetId = worksheetId
        self.connection = connection
        self.engine = engine
        self.schema = schema
        self.tableName = 'movements'
        
    def writeMovements(self):
        start_time = time()
        print('\nWriting database...')
        
        try:
            list_objMovements: list[Projection] = AssembleProjection(self.connection, self.engine, self.schema, self.tableName).getRegisters()
            list_valuesMovements = TransformObj().objects_to_values(list_objMovements)
            GoogleSheets().updateWorksheet_byID(worksheetId=self.worksheetId, list_values=list_valuesMovements, sheetName='Tabela Movimentação', range='A2')
            status = 'Complete'
        except Exception as e:
            status = 'Failed'
            logging.error(f'{" "* 3} Erro: {e}')
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
            
    def writePrices(self):
        
        repositoryPrices = RepositoryPrices(self.connection, self.engine, self.schema, self.tableName)
        start_time = time()
        print('\nWriting prices...')
        try:
            list_prices: list[Projection_Price] = repositoryPrices.getProjection()
            list_valuesPrices = TransformObj().objects_to_values(list_prices)
            GoogleSheets().updateWorksheet_byID(worksheetId=self.worksheetId, list_values=list_valuesPrices, sheetName='Tabela Preços', range='A2')
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
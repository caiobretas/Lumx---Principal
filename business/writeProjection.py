from datetime import datetime
import logging
from time import time
from entities.entityProjection import Projection, Projection_Price
from business.transformObjDict import TransformObj
from business.assembleProjection import AssembleProjection
from repositories.repositoryPrices import RepositoryPrices
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
import pandas as pd
# from viewers.viewerProjection import ViewerProjection

class WriteProjection:
    def __init__(self, worksheetId, connection, engine):
        
        self.worksheetId = worksheetId
        self.connection = connection
        self.engine = engine
        self.tableName = 'movements'
        self.sheetMovementsProjection = 'Tabela Realizados'
        self.sheetPricesProjection = 'Tabela Preços'
        self.sheetUpdates = 'Registro Atualizações'
        
    def writeTransactions(self):
        start_time = time()
        print('\nWriting database...')
        
        headers = ['id', 'data_liquidação','data_vencimento','valorprevisto','valorrealizado','moeda','cotação','valorprevisto_BRL','valorrealizado_BRL','realizado','recorrencia','de','para','percentualrateio','nomecentrocusto','nomepessoa','observacao','descricao','numeronotafiscal','contaativo','projeto','subcategoria4','subcategoria3','subcategoria2','subcategoria','categoria','categoriaprojecao','categoriacusto_receita','hash','check_conciliadoorigem','check_conciliadodestino','produto']
        
        try:
            list_objMovements: list[Projection] = AssembleProjection(self.connection, self.engine).getRegisters()
            list_valuesMovements = TransformObj().objects_to_values(list_objMovements)
            GoogleSheets().overwriteWorksheet_byID(self.worksheetId, list_valuesMovements, self.sheetMovementsProjection, headers=headers, range='A2')
            GoogleSheets().appendRow(values=[self.sheetMovementsProjection,datetime.now().strftime("%d/%m/%Y %H:%M:%S")], sheetName=self.sheetUpdates, worksheetId=self.worksheetId)
            status = 'Complete'
        except Exception as e:
            status = 'Failed'
            logging.error(f'{" "* 3} Erro: {e}')
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
            
    def writePrices(self):
        repositoryPrices = RepositoryPrices(self.connection, self.engine)
        start_time = time()
        print('\nWriting prices...')
        
        headers =['id', 'date', 'token', 'price']
        
        try:
            list_prices: list[Projection_Price] = repositoryPrices.getProjection()
            list_valuesPrices = TransformObj().objects_to_values(list_prices)
            GoogleSheets().overwriteWorksheet_byID(worksheetId=self.worksheetId, list_values=list_valuesPrices, headers=headers,sheetName=self.sheetPricesProjection, range='A2')
            GoogleSheets().appendRow(values=[self.sheetPricesProjection,datetime.now().strftime("%d/%m/%Y %H:%M:%S")], sheetName=self.sheetUpdates, worksheetId=self.worksheetId)
            status = 'Complete'
        except Exception as e:
            status = 'Failed'
            logging.error(f'{" "* 3} Erro: {e}')
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
import string
import logging
from time import sleep
from pandas import DataFrame
from gspread import Worksheet
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from repositories.repositoryBase import RepositoryBase
from entities.entityCategory import Category

class RepositoryCategories( RepositoryBase ):
    def __init__(self, connection, engine: str):
        self.schema = 'finance' # postgresql
        self.tableName = 'categories' # postgresql
        super().__init__(connection,engine,self.schema,self.tableName)
        
        self.controllerGoogleSheets = GoogleSheets()
        self.worksheetName = 'categories' # excel
        
        self.workSheetId = '1oXBOgSVcx3zWYpb0-i16Ykxce5E2ZFoZe-5NEONmZ4k'
        self.workSheetHeaders = [
            'categoriacustoreceita',
            'categoriaprojecao',
            'categoria',
            'subcategoria',
            'subcategoria2',
            'subcategoria3',
            'subcategoria4',
            'projeto',
            'produto',
            'recorrência',
            'method_id',
            'id'
        ]
        self.categoriesSheetId = 1088169641
        self.lastUpdateSheetId = 1239069114
        
    def insertCategories(self, list_category: list[Category]| None):
        if list_category != None:
            values = [t.to_tuple() for t in list_category]
            with self.connection.cursor() as cur:
                try:
                    placeholders = ','.join(['%s'] * len(values[0]))
                    query = f"""
                        INSERT INTO {self.schema}.{self.tableName}
                        (id, recorrencia, projeto, produto, method_id, subcategoria4, subcategoria3,
                        subcategoria2,subcategoria,categoria,categoriaprojecao,
                        categoriacustoreceita)
                        VALUES ({placeholders})
                        ON CONFLICT (id) DO UPDATE SET 
                        recorrencia = EXCLUDED.recorrencia,
                        projeto = EXCLUDED.projeto,
                        produto = EXCLUDED.produto,
                        method_id = EXCLUDED.method_id,
                        subcategoria4 = EXCLUDED.subcategoria4,
                        subcategoria3 = EXCLUDED.subcategoria3, 
                        subcategoria2 = EXCLUDED.subcategoria2,
                        subcategoria = EXCLUDED.subcategoria,
                        categoria = EXCLUDED.categoria,
                        categoriaprojecao = EXCLUDED.categoriaprojecao,
                        categoriacustoreceita = EXCLUDED.categoriacustoreceita"""

                    cur.executemany(query, values)
                    self.connection.commit()
    
                except Exception as e:
                    logging.error(f"{e}")
                    return None
        else:
            return None
        
    def getCategories_fromExcel(self) -> list[Category] | None:
        df: DataFrame = super().openDataFrame()
        if not df.empty:       
            try:
                df.fillna(value="", inplace=True)
                list_aux: list[Category] = []
                for index, row in df.iterrows():
                    row = Category(
                        id = row['id'],
                        recorrencia = row['recorrência'],
                        projeto = row['projeto'],
                        produto = row['produto'],
                        method_id = row['method_id'],
                        subcategoria4 = row['subcategoria4'],
                        subcategoria3 = row['subcategoria3'],
                        subcategoria2 = row['subcategoria2'],
                        subcategoria = row['subcategoria'],
                        categoria = row['categoria'],
                        categoriaprojecao = row['categoriaprojecao'],
                        categoriacustoreceita= row['categoriacustoreceita']
                        )
                    list_aux.append(row)
                return list_aux
            except Exception as e:
                logging.error(f'Erro: {e}')
                return None
            
    def getCategories_fromSheets(self) -> list[Category] | None:
        
        sheet: Worksheet = self.controllerGoogleSheets.openSheet(self.workSheetId, self.categoriesSheetId)
        
        maxColumn = len(self.workSheetHeaders)
        alphabet = string.ascii_uppercase
        index = (maxColumn - 1) % 26
        letter = alphabet[index]
        self.workSheetrange = f"A:{letter}"
        
        row_list: list = sheet.get(self.workSheetrange)
        row_numbers = len(row_list) - 1
        if row_numbers == 0:
            return
        if row_list: row_list.pop(0)
        
        self.controllerGoogleSheets.eraseSheet(self.workSheetId,self.lastUpdateSheetId, self.workSheetHeaders)
        self.controllerGoogleSheets.eraseSheet(self.workSheetId,self.categoriesSheetId, self.workSheetHeaders)
        
        categories: list[Category] = []
        filteredRows = []
        for row in row_list:
            _index = row_list.index(row)
            if not row or row[11] == '':
                continue
            
            table_range = f'A{row_numbers}:{letter}{row_numbers}'
            
            if row != self.workSheetHeaders:
                
                category = Category(id = row[11],method_id = row[10],recorrencia = row[9],produto = row[8],projeto = row[7],subcategoria4 = row[6],subcategoria3 = row[5],subcategoria2 = row[4],subcategoria = row[3],categoria = row[2],categoriaprojecao = row[1],categoriacustoreceita = row[0])
                if category.id:
                    categories.append(category)
                    if row not in filteredRows: filteredRows.append(row)
        
        self.controllerGoogleSheets.openSheet(self.workSheetId,self.lastUpdateSheetId)
        self.controllerGoogleSheets.writemanyRows(filteredRows)
        return categories if row_list else None
    
import logging
from pandas import DataFrame
from interfaces.interfaceBase import InterfaceBase
from entities.entityCategory import Category

class InterfaceCategories(InterfaceBase):
    def __init__(self, pathIF, sheetName):
        super().__init__(path=pathIF, sheetName=sheetName)
    
    def getCategories(self) -> list[Category] | None:
        df: DataFrame = super().abreDataFrame()
        if df.empty == False:
            
            try:
                df.fillna(value="", inplace=True)
                list_aux: list[Category] = []
                for index, row in df.iterrows():
                    row = Category(
                        id = row['id'],
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
                print('Error getting categories')
                raise Exception
        else:
            return None

from pandas import DataFrame
from interfaces.interfaceBase import InterfaceBase
from entities.entityCategory import Category

class InterfaceCategories(InterfaceBase):
    def __init__(self, pathIF, sheetName):
        super().__init__(path=pathIF, sheetName=sheetName)
    
    def getCategories(self) -> list[Category] | Exception:
        df: DataFrame = super().abreDataFrame()
    
        try:
            list_aux: list[Category] = []
            for index, row in df.iterrows():
                row = Category(id = row['id'],
                subcategoria4 = row['subcategoria4'],
                subcategoria3 = row['subcategoria3'],
                subcategoria2 = row['subcategoria2'],
                subcategoria = row['subcategoria'],
                categoria = row['categoria'],
                categoriaprojecao = row['categoriaprojecao'])
                list_aux.append(row)
            return list_aux
        except:
            print('Error getting categories')
            raise Exception

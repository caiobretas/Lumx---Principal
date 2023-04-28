from pandas import DataFrame
from interfaces.interfaceBase import InterfaceBase
from entities.entityConciliation import Conciliation

class InterfaceConciliations(InterfaceBase):
    def __init__(self, pathIF, sheetName='conciliations'):
        super().__init__(path=pathIF, sheetName=sheetName)
    
    def getConciliations(self) -> list[Conciliation] | Exception:
        df: DataFrame = super().abreDataFrame()
    
        try:
            list_aux: list[Conciliation] = []
            for index, row in df.iterrows():
                row = Conciliation(
                hash = row['hash'],
                methodid = row['methodid'],
                description = row['description'],
                project = row['project'],
                )
                list_aux.append(row)
            return list_aux
        except:
            print('Error getting conciliations')
            raise Exception
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
            df.fillna(value=0, inplace=True)
            for index, row in df.iterrows():
                row = Conciliation(
                hash = row['hash'] if row['hash'] != 0 else None,
                methodid = row['methodid'] if row['methodid'] != 0 else None,
                description = row['description'] if row['description'] != 0 else None,
                )
                list_aux.append(row)
            return list_aux
        except:
            print('Error getting conciliations')
            raise Exception
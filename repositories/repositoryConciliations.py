from pandas import DataFrame
from repositories.repositoryBase import RepositoryBase
from entities.entityConciliation import Conciliation

class RepositoryConciliations(RepositoryBase):
    def __init__(self, connection, engine):
        self.schema = 'finance'
        self.sheetName = 'conciliations'
        super().__init__(connection,engine,self.schema,self.sheetName)
    
    def getConciliations_fromExcel(self) -> list[Conciliation] | Exception: # excel
        df: DataFrame = super().openDataFrame()
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
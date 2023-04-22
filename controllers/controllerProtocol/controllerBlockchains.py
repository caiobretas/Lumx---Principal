from pandas import DataFrame

from .controllerProtocol import ControllerProtocol

from entities.entityBlockchain import Blockchain

class ControllerBlockchain( ControllerProtocol ):
    def __init__(self, connection):
        super().__init__(connection)
    
    def getBlockchain(self):
        query = 'select * from blkx.blockchains'
        df: DataFrame = self.run_query(query=query)

        lst_aux: list[Blockchain] = []
        for index, row in df.iterrows():
            row = Blockchain(
            id = row['id'],
            name = row['name'],
            symbol = row['symbol'],
            secret_type = row['secret_type']
            )
            lst_aux.append(row)
            
        return lst_aux
from pandas import DataFrame

from .controllerProtocol import ControllerProtocol
from entities.entityMintRequest import MintRequest

class ControllerMintRequests ( ControllerProtocol ):
    def __init__(self, connection):
        super().__init__(connection)
    
    # retorna uma lista com os requests de mint
    def get_mintRequests(self):
        query = 'select * from blkx.mint_requests'
        df: DataFrame = self.run_query(query)
        list_aux: list[MintRequest] = []
        for index, row in df.iterrows():
            row = MintRequest(id = row['id'],
                              price = row['price'],
                              created_at = row['created_at'],
                              item_id = row['item_id'],
                              txhash = row['txhash'],
                              amount = row['amount'],
                              collection_id = row['collection_id'],
                              wallet_id = row['wallet_id'],
                              status_id = row['status_id']
                              )
            list_aux.append(row)            
        return list_aux

from pandas import DataFrame

from .controllerProtocol import ControllerProtocol

from entities.entityCollection import Collection

class ControllerCollections ( ControllerProtocol ):
    
    def __init__(self, connection):
        super().__init__(connection)

    def get_Collections(self):
        query = 'select * from blkx.collections'
        df: DataFrame = self.run_query(query=query)
        
        list_aux: list[Collection] = []
        for index, row in df.iterrows():
            row = Collection(
            id = row['id'] ,
            client_id = row['client_id'] ,
            name = row['name'] ,
            description = row['description'] ,
            banner_url = row['banner_url'] ,
            contract_id = row['contract_id'] ,
            image_url = row['image_url'] ,
            crossmint_id = row['crossmint_id'] ,
            currency = row['currency'] ,
            random_description = row['random_description'] ,
            random_image_url = row['random_image_url'] ,
            random_item_name = row['random_item_name'] ,
            send_matic = row['send_matic'] 
            )
            list_aux.append(row)
        return list_aux
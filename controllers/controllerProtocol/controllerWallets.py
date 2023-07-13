from pandas import DataFrame

from .controllerProtocol import ControllerProtocol

from entities.protocol.entityWallet import Wallet

class ControllerWallets( ControllerProtocol ):
    def __init__(self, connection):
        super().__init__(connection)
    
    def get_Wallets(self):
        query = 'select * from blkx.wallets'
        df: DataFrame = self.run_query(query=query)

        list_aux: list[Wallet] = []
        for index, row in df.iterrows():
            row = Wallet(
            id = row['id'],
            user_id = row['user_id'],
            address = row['address'],
            external_id = row['external_id'],
            provider = row['provider'],
            pin_code = row['pin_code'],
            created_at = row['created_at'],
            updated_at = row['updated_at'],
            is_archived = row['is_archived']
            )
            list_aux.append(row)
            
        return list_aux
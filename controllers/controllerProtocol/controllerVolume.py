from pandas import DataFrame

from .controllerProtocol import ControllerProtocol
from entities.entityVolume import Volume, VolumeWallets

class ControllerVolume ( ControllerProtocol ):
    def __init__(self, connection):
        super().__init__(connection)
      
    def get_VolumePrimario(self):

        query = """
    SELECT DISTINCT *
FROM (
  SELECT a.id, a.txhash, b.id as collection_id, a.created_at, a.price, a.amount, b.currency, d.symbol as blockchain, a.status_id
  FROM blkx.mint_requests as a, blkx.collections as b, blkx.contracts as c, blkx.blockchains as d, blkx.clients as e
  WHERE a.collection_id = b.id AND b.contract_id = c.id AND c.blockchain_id = d.id
) AS subquery
ORDER BY subquery.created_at DESC;
"""
        try:
            df: DataFrame = self.run_query(query)

        except:
            raise Exception

        list_aux: list[Volume] = []
        try:
            for index, row in df.iterrows():
                row = Volume(
                    id = row['id'],
                    txhash = row['txhash'],
                    datetime = row['created_at'],
                    collection_id = row['collection_id'],
                    type = 'primary',
                    price = row['price'],
                    amount = row['amount'],
                    currency= row['currency'],
                    blockchain = row['blockchain'],
                    status_id = row['status_id'])
                list_aux.append(row)            

            return list_aux
        
        except Exception as e:
            print(e)

    def get_VolumeSecundario(self):
        query = """
        SELECT DISTINCT *
FROM (
    SELECT a.id, a.updated_at, a.status_id, c.id AS collection_id, a.price, c.currency, e.symbol AS blockchain
FROM blkx.listings AS a, blkx.items AS b, blkx.collections AS c, blkx.contracts AS d, blkx.blockchains AS e, blkx.clients AS f
WHERE a.item_id = b.id AND b.collection_id = c.id AND c.contract_id = d.id AND d.blockchain_id = e.id
) AS SUBQUERY
ORDER BY SUBQUERY.updated_at DESC;
"""
        try:
            df: DataFrame = self.run_query(query)

        except:
            raise Exception

        list_aux: list[Volume] = []

        try:
            for index, row in df.iterrows():
                row = Volume(
                id = row['id'],
                txhash = None,
                datetime = row['updated_at'],
                collection_id = row['collection_id'],
                type = 'secondary',
                price = row['price'],
                amount = 1,
                currency= row['currency'],
                blockchain = row['blockchain'],
                status_id = row['status_id'],
                )
                list_aux.append(row)            
            return list_aux
        
        except Exception as e:
            print(e)

    def get_VolumeWallets(self):
        query = """
        SELECT DISTINCT *
FROM(
    SELECT a.id, c.id AS client_id, a.updated_at, a.address, a.provider, a.is_archived
FROM blkx.wallets AS a, blkx.users as b, blkx.clients AS c
WHERE a.user_id = b.id AND b.client_id = c.id
) AS SUBQUERY
ORDER BY SUBQUERY.updated_at DESC;
"""
        try:
            df: DataFrame = self.run_query(query)

        except:
            raise Exception

        list_aux: list[VolumeWallets] = []

        try:
            for index, row in df.iterrows():
                row = VolumeWallets(
                id = row['id'],
                client_id = row['client_id'],
                updated_at = row['updated_at'],
                address = row['address'],
                provider = row['provider'],
                is_archived = row['is_archived'],
                )
                list_aux.append(row)            
            return list_aux
            
        except Exception as e:
            print(e)

    def get_Volumes(self):
        lst_aux = []
        self.get_VolumePrimario()
        self.get_VolumeSecundario()
        lst_aux.extend(self.get_VolumePrimario())
        lst_aux.extend(self.get_VolumeSecundario())
        return lst_aux
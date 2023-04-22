from pandas import DataFrame

from .controllerProtocol import ControllerProtocol

from entities.entityProject import Project

class ControllerProjects ( ControllerProtocol ):
    def __init__(self, connection):
        super().__init__(connection)
    
    def get_Projects(self):

        query = """select a.id as collection_id, a.name as collection_name, b.id as client_id, b.name as client_name, c.royalties as client_royalties, c.royalties_address as client_royalties_address, c.contract_address, d.symbol as blockchain_symbol 
from blkx.collections as a, blkx.clients as b, blkx.contracts as c, blkx.blockchains as d
where a.client_id = b.id and a.contract_id = c.id and c.blockchain_id = d.id
order by a.name ASC;
"""
        df: DataFrame = self.run_query(query=query)
        lst_aux: list[Project] = []
        for index, row in df.iterrows():
            row = Project(
            collection_id = row['collection_id'],
            collection_name = row['collection_name'],
            client_id = row['client_id'],
            client_name = row['client_name'],
            client_royalties = row['client_royalties'],
            client_royalties_address = row['client_royalties_address'],
            contract_address = row['contract_address'],
            blockchain_symbol = row['blockchain_symbol'])
            
            lst_aux.append(row)
        
        return lst_aux
    
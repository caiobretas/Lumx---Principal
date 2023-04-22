from entities.entityVolume import VolumeWallets
from repositories.repositoryBase import RepositoryBase
from pandas import DataFrame

class RepositoryWallets( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
        super().__init__(connection, engine, schema, tableName)
        self.tableName = tableName
        self.schema = schema
    
    def getVolumeWallets(self) -> list[VolumeWallets]:
    
        query =f"""
select date(datetime) as datetime, client_id, cast(count(address) as int) as address, provider, is_archived
from {self.schema}.{self.tableName} as pw
group by client_id, date(datetime), provider, is_archived
order by datetime desc, client_id asc
"""

        df: DataFrame = self.run_query(query=query)

        lst_aux: list[VolumeWallets] = []
        for index, row in df.iterrows():
            row = VolumeWallets(
                id = None,
                client_id = row['client_id'],
                updated_at = row['datetime'],
                address = row['address'],
                provider = row['provider'],
                is_archived = row['is_archived'])
            row.datetime.strftime('%Y/%m/%d')
            lst_aux.append(row)
        return lst_aux

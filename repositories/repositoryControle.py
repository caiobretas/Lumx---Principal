from pandas import DataFrame
from repositories.repositoryBase import RepositoryBase
from entities.entityControle import Controle

class RepositoryControle( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
        super().__init__(connection, engine, schema, tableName)
        self.schema = schema

    def getControle(self) -> list[Controle]:
        query = f"""
select distinct
	coalesce(date(pw.datetime), date(pv.datetime)) as date,
  coalesce(p.client_id, pw.client_id) as client_id,
  coalesce(p2.client_name, p.client_name) as client_name
  
from {self.schema}.projects_volumes as pv
left join {self.schema}.projects as p on pv.collection_id = p.id
full outer join {self.schema}.projects_wallets as pw on date(pv.datetime) = date(pw.datetime) and pw.client_id = p.client_id
left join {self.schema}.projects as p2 on p2.client_id = pw.client_id
order by date desc;
"""
        df: DataFrame = self.run_query(query=query)

        lst_aux: list[Controle] = []
        for index, row in df.iterrows():
            row = Controle(
                date = row['date'],
                client_id = row['client_id'],
                client_name = row['client_name'])
            lst_aux.append(row)
        
        return lst_aux

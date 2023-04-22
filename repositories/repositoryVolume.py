from pandas import DataFrame
from repositories.repositoryBase import RepositoryBase
from entities.entityVolume import Volume, VolumeWallets 

class RepositoryVolume ( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
        super().__init__(connection=connection, engine=engine, schema=schema, tableName=tableName)

        self.schema = schema
    
    # falta inserir via query (problema dos atributos indesejados no db)
    def insereVolume(self, lst: list[Volume]):
        super().salvaDatabase(lst)

    def getVolume(self) -> list[Volume]:
        query = f"""
CREATE TEMPORARY TABLE IF NOT EXISTS prices as
  SELECT subqueryB.time, POWER(c.close, -1) * subqueryB.close as close, subqueryB.conversionSymbol, subqueryB.date
  FROM {self.schema}.prices_crypto as c
  RIGHT JOIN (
      SELECT time, close, conversionSymbol, date
      FROM {self.schema}.prices_crypto
  	) AS subqueryB on c.time = subqueryB.time
  WHERE c.conversionsymbol = 'BRL';
  
CREATE TEMPORARY TABLE IF NOT EXISTS volume as
  select pv.id, pv.txhash, pv.datetime, pv.collection_id, pv.type, projects.client_id, pv.status_id, pv.price, pv.amount, pv.currency, pv.blockchain, p.close
  from {self.schema}.projects_volumes as pv
  left join prices as p on pv.blockchain = p.conversionsymbol and date(pv.datetime) = date(p.date)
  left join {self.schema}.projects on projects.id = pv.collection_id
  order by datetime desc;
  select * from volume;
  """
        df: DataFrame = self.run_query(query=query)

        lst_aux: list[Volume] = []
        for index, row in df.iterrows():
            row = Volume(
                id = row['id'],
                txhash = row['txhash'],
                datetime = row['datetime'],
                collection_id = row['collection_id'],
                type = row['type'],
                price = row['price'],
                amount = row['amount'],
                currency = row['currency'],
                blockchain = row['blockchain'],
                status_id = row['status_id'])
            
            row.client_id = df.loc[index, 'client_id']
            row.coinPrice = df.loc[index, 'close']
        
            lst_aux.append(row)
        
        return lst_aux

    def getVolumebyType(self, type, currency = 'crypto'):

        if type == 'primary':
            query = f"""select *
            from finance.projects_volumes
            where type = '{type}' and currency = '{currency}'
            """

        elif type == 'secondary':
            query = f"""select *
            from finance.projects_volumes
            where type = '{type} and status_id = 'success'
            """

        else: raise Exception

        df: DataFrame = self.run_query(query=query)

        lst_aux: list[Volume] = []
        for index, row in df.iterrows():
            row = Volume(
                id = row['id'],
                txhash = row['txhash'],
                datetime = row['datetime'],
                collection_id = row['collection_id'],
                type = row['type'],
                price = row['price'],
                amount = row['amount'],
                currency = row['currency'],
                blockchain = row['blockchain'],
                status_id = row['status_id'])
            lst_aux.append(row)
        
        return lst_aux


    def insereVolumeWallets(self, lst: list[VolumeWallets]):
        super().salvaDatabase(lst)
    
    
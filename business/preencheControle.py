from pandas import DataFrame
from repositories.repositoryBase import RepositoryBase
from entities.entityControle import Controle
from viewers.viewerControle import ViewerControle

class PreencheControle( RepositoryBase ):
    
    def __init__(self, path, lst: list[Controle], connection: str, engine: str, schema: str, tableName=None):
        super().__init__(connection, engine, schema, tableName)
        self.lst = lst
        self.schema = schema
        # falta inserir cláusula para verificar se o valor já está lá. Se estiver, não fazer nada.
        self.lstCalculada = ViewerControle(path=path, sheetName='Controle')
        
    def get_walletsbyDateClient(self):
        try:
            for obj in self.lst:
                query = f"""
SELECT SUM(address) as wallets_onCustody
FROM (
  SELECT DATE(datetime) AS datetime, client_id, CAST(COUNT(address) AS int) AS address, provider, is_archived
  FROM {self.schema}.projects_wallets
  WHERE provider = 'venly' AND is_archived = 'false' AND DATE(datetime) <= '{obj.date}' AND client_id = '{obj.client_id}'
  GROUP BY client_id, DATE(datetime), provider, is_archived
) AS subquery;

    """
                df: DataFrame = self.run_query(query=query)
                if df.empty == False:
                    obj.wallets_onCustody = df.iloc[0][0]
                else:
                    obj.wallets_onCustody = None
        except Exception as e:
            print(f"Erro ao preencher controle: Wallets\n{e}")

    def get_Fiat_Volume_byDateClient(self):
        try:
            for obj in self.lst:

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
    
    select date(datetime) as date, client_id, sum((price * amount)) as fiat_volumePrimary 
    from volume
    where
        date(datetime) = '{obj.date}' and
    client_id = '{obj.client_id}' and
    type = 'primary' and
    currency = 'fiat'
    group by date(datetime), client_id
    ;"""
                df: DataFrame = self.run_query(query=query)
                if df.empty == False:
                    obj.fiat_volumePrimary = df.iloc[0][2]
                else:
                    obj.fiat_volumePrimary = 0
        except Exception as e:
            print(f"Erro ao preencher controle: Volume Primário - Fiat\n{e}")

    def get_Crypto_VolumePrimary_byDateClient(self):
        
        for obj in self.lst:
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
 
  select date(datetime) as date, client_id, sum((price * amount)) as crypto_volumePrimary, blockchain as coin, close as coinPrice
 from volume
 where
 	date(datetime) = '{obj.date}' and
  client_id = '{obj.client_id}' and
  type = 'primary' and
  currency = 'crypto'
  group by date(datetime), client_id, coinPrice, coin
  ;
  """
            df: DataFrame = self.run_query(query=query)
            if df.empty == False:
                obj.crypto_volumePrimary = df.iloc[0][2]
                obj.coin_Primary = df.iloc[0][3]
                obj.coinPrice_volumePrimary = df.iloc[0][4]
                obj.volumePrimary_BRL = obj.fiat_volumePrimary + obj.crypto_volumePrimary * obj.coinPrice_volumePrimary
            else:
                obj.crypto_volumePrimary = 0
                obj.coin_Primary = None
                obj.coinPrice_volumePrimary = None
                obj.volumePrimary_BRL = obj.fiat_volumePrimary
    
    def get_Crypto_VolumeSecondary_byDateClient(self):
            
        for obj in self.lst:
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
 
 select date(datetime) as date,
 client_id,
 SUM((price * amount)) as volume_secondary_crypto,
 blockchain as coin, close as coinPrice
 from volume
 where
 	date(datetime) = '{obj.date}' and
  client_id = '{obj.client_id}' and
  type = 'secondary' and
  status_id = 'success'
  group by date(datetime),
 client_id,
 coin, coinPrice
"""
            df: DataFrame = self.run_query(query=query)
            if df.empty == False:
                obj.crypto_volumeSecondary = df.iloc[0][2]
                obj.coin_Secondary = df.iloc[0][3]
                obj.coinPrice_volumeSecondary = df.iloc[0][4]
                obj.volumeSecondary_BRL = obj.crypto_volumeSecondary * obj.coinPrice_volumeSecondary
            else:
                obj.crypto_volumeSecondary = 0
                obj.coin_Secondary = None
                obj.coinPrice_volumeSecondary = None
                obj.volumeSecondary_BRL = 0
      
    def preencheControle(self):
        self.get_walletsbyDateClient()
        self.get_Fiat_Volume_byDateClient()
        self.get_Crypto_VolumePrimary_byDateClient()
        self.get_Crypto_VolumeSecondary_byDateClient()

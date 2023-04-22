from pandas import DataFrame
from .controllerFinance import ControllerFinance
from entities.entityControle import Controle

class ControllerControle( ControllerFinance ):
    def __init__(self, connection):
        super().__init__(connection)

    def getControleVolume(self):
        query = f"""CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
  SELECT subqueryB.time, POWER(c.close, -1) * subqueryB.close AS close, subqueryB.conversionSymbol, subqueryB.date
  FROM finance.prices_crypto AS c
  RIGHT JOIN (
      SELECT time, close, conversionSymbol, date
      FROM finance.prices_crypto
  	) AS subqueryB ON c.time = subqueryB.time
  WHERE c.conversionsymbol = 'BRL';

create temporary table if not exists volume_primary_fiat as 
  select date(datetime) as date, collection_id, (price * amount) as volume_primary_fiat
  from finance.projects_volumes as pv
    inner join finance.projects as p on p.id = pv.collection_id
 	where currency = 'fiat' and type = 'primary';

create temporary table if not exists volume_primary_crypto as 
  select date(datetime) as date, collection_id, (price * amount) as volume_primary_crypto, (price * amount * close) as volume_primary_crypto_inBRL
  from finance.projects_volumes as pv
    inner join finance.projects as p on p.id = pv.collection_id
    inner join prices as pc on date(pc.date) = date(pv.datetime) and pc.conversionsymbol = pv.blockchain
 	where currency = 'crypto' and type = 'primary';
  
create temporary table if not exists volume_secondary_crypto as 
  select date(datetime) as date, collection_id, (price) as volume_secondary_crypto, (price * close) as volume_secondary_crypto_inBRL
  from finance.projects_volumes as pv
    inner join finance.projects as p on p.id = pv.collection_id
    inner join prices as pc on date(pc.date) = date(pv.datetime) and pc.conversionsymbol = pv.blockchain
 	where type = 'secondary' and status_id = 'success';
 
create temporary table if not exists controle as
    SELECT vpf.date, vpf.collection_id FROM volume_primary_fiat as vpf
    UNION ALL
    SELECT vpc.date, vpc.collection_id FROM volume_primary_crypto as vpc
    UNION ALL
    SELECT vsc.date, vsc.collection_id FROM volume_secondary_crypto as vsc;

select distinct c.date, p.client_id, p.id as collection_id, client_name, p.collection_name
from controle as c
inner join finance.projects as p on p.id = c.collection_id
order by date desc;
"""
        df: DataFrame = self.run_query(query=query)

        lst_aux: list[Controle] = []
        for index, row in df.iterrows():
            row = Controle(
                date = row['date'],
                client_name = row['client_name'],
                client_id = row['client_id'],
                collection_id = row['collection_id'])
            lst_aux.append(row)
        return lst_aux
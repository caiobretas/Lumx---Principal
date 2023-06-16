import logging
import psycopg2
from entities.entityCoin import Coin
from entities.entityProjection import Projection_Price
from repositories.repositoryBase import RepositoryBase

class RepositoryPrices( RepositoryBase ):
    def __init__(self, connection: str, engine):
        self.schema = 'finance' 
        self.tableName = 'prices_crypto'
        self.connection: psycopg2.connection = connection
        
        super().__init__(connection, engine, self.schema, self.tableName)
        
    def getPrices(self) -> list[Coin]:
        with self.connection.cursor() as cur:
            try:
                query = f"""select id,date,high,low,open,volumefrom,volumeto,close,conversiontype,conversionsymbol from {self.schema}.{self.tableName} order by date desc, conversionsymbol desc"""
                cur.execute(query=query)
                listCoins: list[Coin] = []
                for row in cur.fetchall():
                    obj = Coin(id=row[0],
                               date=row[1],
                               high=row[2],
                               low=row[3],
                               open=row[4],
                               volumefrom=row[5],
                               volumeto=row[6],
                               close=row[7],
                               conversiontype=row[8],
                               conversionsymbol=row[9])
                    listCoins.append(obj)
                return listCoins
            
            except:
                raise Exception
            
    def getTokens(self) -> list:
        with self.connection.cursor() as cur:
            try:
                query = f"""select distinct conversionsymbol as token from {self.schema}.{self.tableName} where conversionsymbol != 'BRL'"""
                cur.execute(query=query)
                list_tokens: list = []
                for row in cur.fetchall():
                    list_tokens.extend(row)
                return list_tokens
            except:
                raise Exception

    def getDate(self):
        with self.connection.cursor() as cur:
            try:
                query = f"""select date(max(date)) from {self.schema}.{self.tableName};"""
                cur.execute(query=query)
                self.maxDate = cur.fetchone()[0]
                return self.maxDate
            
            except:
                raise Exception
    
    def insertPrice(self, list_coin: list[Coin]) -> None:
        values = [t.to_tuple() for t in list_coin]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id, time, date, high, low, open, volumefrom,
                    volumeto, close, conversiontype, conversionsymbol)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO
                    UPDATE SET
                    id = EXCLUDED.id,
                    time = EXCLUDED.time,
                    date = EXCLUDED.date,
                    high = EXCLUDED.high,
                    low = EXCLUDED.low,
                    open = EXCLUDED.open,
                    volumefrom = EXCLUDED.volumefrom,
                    volumeto = EXCLUDED.volumeto,
                    close = EXCLUDED.close,
                    conversiontype = EXCLUDED.conversiontype,
                    conversionsymbol = EXCLUDED.conversionsymbol
                    """

                cur.executemany(query, values)
                self.connection.commit()

            except:
                raise Exception

    def deleteByDate(self, date):
        try:
            with self.connection.cursor() as cur:
                query = f"""delete from {self.schema}.{self.tableName}
                WHERE to_char(date, 'YYYY-MM-DD') >= '{date}'"""

                cur.execute(query=query)
                self.connection.commit()
        
        except:
            raise Exception
        
    def getProjection(self) -> list[Projection_Price]:
        with self.connection.cursor() as cur:
            try:
                query = f"""CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
            SELECT
                subqueryB.time, POWER(c.close, -1) * subqueryB.close AS close, subqueryB.conversionSymbol, subqueryB.date
            FROM
                {self.schema}.{self.tableName} AS c
            RIGHT JOIN (
                SELECT
                    time, close, conversionSymbol, date
                FROM
                    {self.schema}.{self.tableName}
                ) AS subqueryB ON c.time = subqueryB.time
            WHERE
                c.conversionsymbol = 'BRL';

select time, close, conversionsymbol, date from prices
order by date desc;

"""
                cur.execute(query=query)
                listProjection_Prices: list[Projection_Price] = []
                for row in cur.fetchall():
                    obj = Projection_Price(
                        date=row[3],
                        token=row[2],
                        close=row[1])
                    listProjection_Prices.append(obj)
                return listProjection_Prices
            except Exception as e:
                logging.error(f'{" "* 3} Erro: {e}')
    
    def getExchangeVariation(self) -> list:
        query = f"""CREATE TEMPORARY TABLE IF NOT EXISTS prices AS SELECT subqueryB.time, POWER(c.close, -1) * subqueryB.close AS close, subqueryB.conversionSymbol, subqueryB.date FROM {self.schema}.{self.tableName} AS c RIGHT JOIN (SELECT time, close, conversionSymbol, date FROM {self.schema}.{self.tableName}) AS subqueryB ON c.time = subqueryB.time WHERE c.conversionsymbol = 'BRL';

create temporary table if not exists exchange_variation as SELECT concat(cast(time as varchar),conversionsymbol) as id, date(date), conversionSymbol,  close - LAG(close) OVER (PARTITION BY conversionSymbol ORDER BY date, conversionSymbol) AS variacaoCambial FROM prices ORDER BY date asc;
select * from exchange_variation where date(date) >= '2022-01-01'
"""
        try:
            with self.connection.cursor() as cur:
                cur.execute(query)
                result_list = []
                result = cur.fetchall()
                for result in result:
                    result_list.append(result)
                return result_list
        
        except Exception as e:
            logging.error(e)
            
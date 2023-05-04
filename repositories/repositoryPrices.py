import psycopg2
from entities.entityCoin import Coin
from repositories.repositoryBase import RepositoryBase

class RepositoryPrices( RepositoryBase ):
    def __init__(self, connection: str, engine, schema, tableName='prices_crypto'):
        super().__init__(connection, engine, schema, tableName)
        self.connection: psycopg2.connection = connection
        self.tableName = tableName
        self.schema = schema
    
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
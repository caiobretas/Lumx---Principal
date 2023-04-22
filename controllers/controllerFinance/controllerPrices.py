from pandas import DataFrame
from .controllerFinance import ControllerFinance
from entities.entityCoin import Coin

class ControllerPrices ( ControllerFinance ):
    def __init__(self, connection, schema, tableName):
        super().__init__(connection)
        self.schema = schema
        self.tableName = tableName

    def getPrices(self):
        query =  """CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
  SELECT a.time, a.high, a.low, a.open, a.volumefrom, a.volumeto, POWER(c.close, -1) * a.close AS close, a.conversiontype, a.conversionSymbol, a.date
  FROM finance.prices_crypto AS c
  RIGHT JOIN (
      SELECT *
      FROM finance.prices_crypto
  	) AS a ON c.time = a.time
  WHERE c.conversionsymbol = 'BRL';

select * from prices
where conversionsymbol != 'BRL'
order by time desc;"""

        df: DataFrame = self.run_query(query=query)

        lst_aux: list[Coin] = []
        for index, row in df.iterrows():
            row = Coin(
                id = None,
                time = row['time'],
                high = row['high'],
                low = row['low'],
                open = row['open'],
                volumefrom = row['volumefrom'],
                volumeto = row['volumeto'],
                close = row['close'],
                conversiontype = row['conversiontype'],
                conversionsymbol = row['conversionsymbol'],
                date = row['date'])
            lst_aux.append(row)
        
        return lst_aux


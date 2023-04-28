import csv
from io import StringIO
from datetime import datetime
from entities.entityTransaction import TransactionCrypto
from entities.entityCoin import Coin
from entities.entityProjection import Projection
from repositories.repositoryBase import RepositoryBase
import psycopg2

class RepositoryCryptoTransaction ( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
        self.tableName = tableName
        self.schema = schema
        self.connection: psycopg2.connection = connection
        super().__init__(connection, engine, schema, tableName)

    def getDate(self) -> datetime:
        with self.connection.cursor() as cur:
            try:
                query = f"""
                select date(max(datetime)) as data from {self.schema}.{self.tableName}"""
                cur.execute(query)
                return cur.fetchone()[0]
            except Exception as e:
                print(e)
                raise e
                       
    def insert(self, lst: list[TransactionCrypto]) -> None:
        with self.connection.cursor() as cur:
            values = [t.to_tuple() for t in lst]
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id, blockNumber, blockHash, datetime, hash, nonce, from_, to_,
                    contractAddress, gas, gasPrice, gasUsed, cumulativeGasUsed, value, gasFee, total,
                    tokenName, tokenSymbol, tokenDecimal, isError, txreceipt_status, type,
                    methodId, functionName, txnType, blockchain, address, bank, scan, description) VALUES ({placeholders})
                    ON CONFLICT (id) DO NOTHING
                    ;"""
                    
                cur.executemany(query, values)
                self.connection.commit()
            
            except Exception as e:
                print(e)
                print(f'\nProblem inserting crypto transactions')
                raise e

    # def insert_reset(self, lst: list[TransactionCrypto]) -> None:
    #     with self.connection.cursor() as cur:
    #         csv_data = StringIO()
    #         writer = csv.writer(csv_data)
    #         for t in lst:
    #             writer.writerow(t.to_tuple())
    #         csv_data.seek(0)
            
    #         try:
    #             cur.copy_from(csv_data, f"{self.schema}.{self.tableName}", sep=",", columns=YOUR_COLUMN_NAMES)
    #         self.connection.commit()
        
    #     except Exception as e:
    #         print(e)
    #         print(f'\nProblem inserting crypto transactions')
    #         raise e

    def deleteByDate(self, date)-> None:
        with self.connection.cursor() as cur:
            try:
                query = f"""delete from {self.schema}.{self.tableName} WHERE date(datetime) = '{date}'"""
                cur.execute(query=query)
                self.connection.commit()
            except:
                raise Exception
    
    def delete_unknown_tokens(self, list_known_tokens: list[Coin]):
        lista_valores = ','.join("'" + str(item) + "'" for item in list_known_tokens)
        with self.connection.cursor() as cur:
            try:
                query = f"""DELETE from {self.schema}.{self.tableName}
                where tokensymbol not in ({lista_valores})
                """
                cur.execute(query=query)
                self.connection.commit()
            except:
                raise Exception
            
    def getProjection(self) -> list[Projection]:
        with self.connection.cursor() as cur:
             
            query = f"""CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
  SELECT subqueryB.time, POWER(c.close, -1) * subqueryB.close AS close, subqueryB.conversionSymbol, subqueryB.date
  FROM {self.schema}.prices_crypto AS c
  RIGHT JOIN (
      SELECT time, close, conversionSymbol, date
      FROM {self.schema}.prices_crypto
  	) AS subqueryB ON c.time = subqueryB.time
  WHERE c.conversionsymbol = 'BRL';

select
m.id, m.hash, m.datetime, m.total, m.tokensymbol, pc.close, (m.total * pc.close) as total_BRL,
b.name as de, b1.name as para, m.bank as contaativo, c.subcategoria4, c.subcategoria3,
c.subcategoria2, c.subcategoria, c.categoria, c.categoriaprojecao

from {self.schema}.{self.tableName} as m
	left join {self.schema}.categories as c on m.methodid = c.method_id
  left join {self.schema}.book as b on m.from_ = b.address
  left join {self.schema}.book as b1 on m.to_ = b1.address
  left join prices as pc on pc.conversionsymbol = m.tokensymbol and date(pc.date) = date(m.datetime)
  order by date desc, tokensymbol asc;
"""
            try:
                cur.execute(query=query)
                list_projection: list[Projection] = []
                for row in cur.fetchall():
                    register = Projection(
                    id = row[0],
                    data_lançamento = row[2].date() if type(row[2]) == datetime else None,
                    data_liquidação = row[2].date() if type(row[2]) == datetime else None,
                    datavencimento = row[2].date() if type(row[2]) == datetime else None,
                    valorprevisto = row[3],
                    valorrealizado = row[3],
                    moeda = row[4],
                    cotação = row[5],
                    valorprevisto_BRL = row[6],
                    valorrealizado_BRL = row[6],
                    realizado = 1,
                    recorrente = None,
                    de = row[7],
                    para = row[8],
                    percentualrateio = None,
                    nomecentrocusto = None,
                    nomepessoa = None,
                    observacao = None,
                    descricao = None,
                    numeronotafiscal = None,
                    contaativo = row[9],
                    subcategoria4 = row[10],
                    subcategoria3 = row[11],
                    subcategoria2 = row[12],
                    subcategoria = row[13],
                    categoria = row[14],
                    categoriaprojecao = row[15],
                    categoriacusto_receita = None,
                    hash = row[1],
                    check_conciliadoorigem = 1,
                    check_conciliadodestino = 1,
                    projeto = None
                    )
                    list_projection.append(register)
                    
                self.connection.commit()
                return list_projection
            except:
                raise Exception

    def conciliate_withExcel(self) -> None:
        with self.connection.cursor() as cur:
            try:
                query = f"""UPDATE {self.schema}.{self.tableName}
                SET methodid = methodid,
                """
                cur.execute(query=query)
                self.connection.commit()
            except:
                raise Exception
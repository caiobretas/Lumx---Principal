from datetime import datetime
from entities.entityTransaction import TransactionCrypto
from entities.entityCoin import Coin
from repositories.repositoryPrices import RepositoryPrices
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
                    methodId, functionName, txnType, blockchain, address, bank, scan) VALUES ({placeholders})
                    ON CONFLICT (id) DO NOTHING
                    ;"""
                    
                cur.executemany(query, values)
                self.connection.commit()
            
            except Exception as e:
                print(e)
                print(f'\nProblem inserting crypto transactions')
                raise e

    def deleteByDate(self, date):
        
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
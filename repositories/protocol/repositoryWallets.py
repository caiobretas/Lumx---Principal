from datetime import datetime
import logging
from repositories.repositoryBase import RepositoryBase
from entities.protocol.entityWallet import Wallet

class RepositoryWallets ( RepositoryBase ):
    def __init__(self, connection, engine):
        
        self.schema = 'blkx'
        self.tableName = 'wallets'

        super().__init__(connection, engine, self.schema, self.tableName)
        
        self.wallets: list[Wallet] = []
    
    def getWallets(self):
            
        query = f"""select id,user_id,address,external_id,provider,pin_code,created_at,updated_at,is_archived from {self.schema}.{self.tableName}""" 
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                for row in cursor.fetchall():
                    wallet = Wallet(                        
                    id = row[0],
                    user_id = row[1],
                    address = row[2],
                    external_id = row[3],
                    provider = row[4],
                    pin_code = row[5],
                    created_at = row[6],
                    updated_at = row[7],
                    is_archived = row[8]
                    )
                    self.wallets.append(wallet)
            return self.wallets
        except IndexError as ie:
            print(f"Error: {ie} - Local: Repository Wallets")
        
    def runQuery(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.wallets = []
                for row in cursor.fetchall():
                    row_list = list(row)
                    converted_row = []
                    for value in row_list:
                        if isinstance(value, datetime):
                            converted_row.append(value.strftime('%Y-%m-%d %H:%M:%S'))
                        else:
                            converted_row.append(value)
                    self.wallets.append(tuple(converted_row))
            return self.wallets
        except Exception as e:
            logging.error(e)

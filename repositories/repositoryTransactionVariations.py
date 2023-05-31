import psycopg2
import logging
from typing_extensions import Literal
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from entities.entityTransaction import Transaction
from entities.entityProjection import Projection
from entities.entityBankAccount import BankAccount
from repositories.repositoryBase import RepositoryBase
from sqlalchemy import MetaData


class RepositoryTransaction ( RepositoryBase ):
    def __init__(self, connection: str, engine: str):
        self.tableName = 'movements'
        self.schema = 'finance'
        self.connection = connection
        
        self.transactions = []
        
        super().__init__(connection, engine, self.schema, self.tableName)
    
                       
    def insert(self, obj: list[Transaction] | Transaction, method: Literal['bulk', 'single'] = 'bulk') -> None:
        
        with self.connection.cursor() as cur:
            method = method.lower()
            if method == 'bulk' and type(obj) == list:
                values = [t.to_tuple() for t in obj]
                placeholders = ','.join(['%s'] * len(values[0]))
            if method == 'single':
                values = obj.to_tuple()
                placeholders = ','.join(['%s'] * len(values))
            try:
                query = f"""INSERT INTO {self.schema}.{self.tableName}
                (id, tipo, data, datapagamento, datavencimento, datacompetencia, valorprevisto, valorrealizado, percentualrateio, realizado, idcontaorigem, nomecontaorigem, codigoreduzidoorigem, idcontadestino, nomecontadestino, codigoreduzidodestino,  idcentrocusto, nomecentrocusto, idpessoa, nomepessoa, observacao, cpfcnpjpessoa, descricao, idunidadenegocio, nomeunidadenegocio, numeronotafiscal, conciliadoorigem, conciliadodestino, saldoiniciodiacontaativo, saldofimdiaccontaativo, idprojeto, nomeprojeto, idclassificacao, contaativo, idkamino)
                VALUES ({placeholders})
                on conflict (idKamino) do nothing;"""
                    
                cur.executemany(query, values) if method == 'bulk' else cur.execute(query, values)
                self.connection.commit()
            
            except Exception as e:
                logging.error(e)
                print(f'\nNo new transactions found')
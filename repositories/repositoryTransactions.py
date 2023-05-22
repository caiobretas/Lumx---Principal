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
        self.tableName = 'movements2'
        self.schema = 'finance'
        self.connection: psycopg2.connection = connection
        self.metadata = MetaData(schema=self.schema)
        
        self.transactions = []
        
        super().__init__(connection, engine, self.schema, self.tableName)
        
    def getMetadata(self) -> tuple:
        try:
            table = self.metadata.tables[self.tableName]
            columns = table.columns
            return table, columns
        except Exception as e:
            logging.error(e)
            
    def getDate(self, realizado: int = 1) -> datetime:

        with self.connection.cursor() as cur:

            try:
                
                if realizado == 1:
                    query1 = f"""select date(max(data)) as data from {self.schema}.{self.tableName} where realizado = {realizado} order by data desc;"""
                    cur.execute(query1)
                    return cur.fetchone()[0]
 
                elif realizado == 0:
                    query2 = f"""select date(min(data)) as data from {self.schema}.{self.tableName} where realizado = {realizado} order by data desc;"""
                    cur.execute(query2)
                    return cur.fetchone()[0]
            
            except Exception as e:
                logging.error(e)
                       
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
        
    def delete(self, delete_idList) -> None:
        with self.connection.cursor() as cur:
            ids = ','.join(delete_idList)
            try:
                query = f"""
                DELETE FROM
                    {self.schema}.{self.tableName}
                WHERE
                    CAST(idkamino AS INTEGER) in ({ids})
                """   
                cur.execute(query)
                self.connection.commit()
            
            except Exception as e:
                logging.error(e)
                print(f'\nNo new transactions found')
    
    def upsert(self, obj: list[Transaction] | Transaction, method: Literal['bulk', 'single'] = 'bulk') -> None:
        method = method.lower()
        if method == 'bulk' and type(obj) == list:
                values = [t.to_tuple() for t in obj]
                placeholders = ','.join(['%s'] * len(values[0]))
        if method == 'single':
            values = obj.to_tuple()
            placeholders = ','.join(['%s'] * len(values))
        with self.connection.cursor() as cur:
            query = f"""
            insert into
                {self.schema}.{self.tableName}
                (id,
                tipo,
                data,
                datapagamento,
                datavencimento,
                datacompetencia,
                valorprevisto,
                valorrealizado,
                percentualrateio,
                realizado,
                idcontaorigem,
                nomecontaorigem,
                codigoreduzidoorigem,
                idcontadestino,
                nomecontadestino,
                codigoreduzidodestino,
                idcentrocusto,
                nomecentrocusto,
                idpessoa,
                nomepessoa,
                observacao,
                cpfcnpjpessoa,
                descricao,
                idunidadenegocio,
                nomeunidadenegocio,
                numeronotafiscal,
                conciliadoorigem,
                conciliadodestino,
                saldoiniciodiacontaativo,
                saldofimdiaccontaativo,
                idprojeto,
                nomeprojeto,
                idclassificacao,
                contaativo,
                idkamino)
            VALUES ({placeholders})
            
            ON CONFLICT (idkamino) DO UPDATE
            SET
                tipo = EXCLUDED.tipo,
                data = EXCLUDED.data,
                datapagamento = EXCLUDED.datapagamento,
                datavencimento = EXCLUDED.datavencimento,
                datacompetencia = EXCLUDED.datacompetencia,
                valorprevisto = EXCLUDED.valorprevisto,
                valorrealizado = EXCLUDED.valorrealizado,
                percentualrateio = EXCLUDED.percentualrateio,
                realizado = EXCLUDED.realizado,
                idcontaorigem = EXCLUDED.idcontaorigem,
                nomecontaorigem = EXCLUDED.nomecontaorigem,
                codigoreduzidoorigem = EXCLUDED.codigoreduzidoorigem,
                idcontadestino = EXCLUDED.idcontadestino,
                nomecontadestino = EXCLUDED.nomecontadestino,
                codigoreduzidodestino = EXCLUDED.codigoreduzidodestino,
                idcentrocusto = EXCLUDED.idcentrocusto,
                nomecentrocusto = EXCLUDED.nomecentrocusto,
                idpessoa = EXCLUDED.idpessoa,
                nomepessoa = EXCLUDED.nomepessoa,
                observacao = EXCLUDED.observacao,
                cpfcnpjpessoa = EXCLUDED.cpfcnpjpessoa,
                descricao = EXCLUDED.descricao,
                idunidadenegocio = EXCLUDED.idunidadenegocio,
                nomeunidadenegocio = EXCLUDED.nomeunidadenegocio,
                numeronotafiscal = EXCLUDED.numeronotafiscal,
                conciliadoorigem = EXCLUDED.conciliadoorigem,
                conciliadodestino = EXCLUDED.conciliadodestino,
                saldoiniciodiacontaativo = EXCLUDED.saldoiniciodiacontaativo,
                saldofimdiaccontaativo = EXCLUDED.saldofimdiaccontaativo,
                idprojeto = EXCLUDED.idprojeto,
                nomeprojeto = EXCLUDED.nomeprojeto,
                idclassificacao = EXCLUDED.idclassificacao,
                contaativo = EXCLUDED.contaativo,
                idkamino = EXCLUDED.idkamino
            """
            try:
                cur.executemany(query, values) if method == 'bulk' else cur.execute(query, values)
                self.connection.commit()
            except Exception as e:
                logging.error(e)
                
    def getTransactions(self, realizado=None) -> list[Transaction]:
        if realizado is None:
           query = f"""
                select * from {self.schema}.{self.tableName}
                order by data desc;
                """
        elif realizado == 1:
            query = f"""
                select * from {self.schema}.{self.tableName}
                where realizado = 1
                order by data desc;
                """
        elif realizado == 0:
            query = f"""
                select * from {self.schema}.{self.tableName}
                where realizado = 0
                order by data desc;
                """
            
        with self.connection.cursor() as cur: 
            
            try:
                list_transactions: list[Transaction] = []
                cur.execute(query)
                for row in cur.fetchall():
                    transaction: Transaction = Transaction(
                    id = row[0],
                    tipo = row[1],
                    data = row[2],
                    datapagamento = row[3],
                    datavencimento = row[4],
                    datacompetencia = row[5],
                    valorprevisto = row[6],
                    valorrealizado = row[7],
                    percentualrateio = row[8],
                    realizado = row[9],
                    idcontaorigem = row[10],
                    nomecontaorigem = row[11],
                    codigoreduzidoorigem = row[12],
                    idcontadestino = row[13],
                    nomecontadestino = row[14],
                    codigoreduzidodestino = row[15],
                    idcentrocusto = row[16],
                    nomecentrocusto = row[17],
                    idpessoa = row[18],
                    nomepessoa = row[19],
                    observacao = row[20],
                    cpfcnpjpessoa = row[21],
                    descricao = row[22],
                    idunidadenegocio = row[23],
                    nomeunidadenegocio = row[24],
                    numeronotafiscal = row[25],
                    conciliadoorigem = row[26],
                    conciliadodestino = row[27],
                    saldoiniciodiacontaativo = row[28],
                    saldofimdiaccontaativo = row[29],
                    idprojeto = row[30],
                    nomeprojeto = row[31],
                    idclassificacao = row[32],
                    contaativo = row[33],
                    idKamino=row[34])
                    list_transactions.append(transaction)

                # desativar o retorno quando fizer a atualização do sistema (pegar transações pelo self após usar o método)
                return list_transactions

            except Exception as e:
                logging.error(e)
                return []

    def deleteByDate(self, date: datetime):
        date_str = date.strftime("%y-%m-%d")
        
        with self.connection.cursor() as cur:
             
            query = f"""DELETE FROM {self.schema}.{self.tableName} WHERE TO_CHAR(data, 'YY-MM-DD') = '{date_str}' AND realizado = 1;"""

            cur.execute(query=query)

            self.connection.commit()

    def deleteFutures(self):
        
        with self.connection.cursor() as cur:
             
            query = f"""delete from {self.schema}.{self.tableName}
        where realizado = 0;"""

            cur.execute(query=query)

            self.connection.commit()
    
    def getProjection(self) -> list[Projection]:
        with self.connection.cursor() as cur:
             
            query = f"""select fm.id, datapagamento as data_liquidação, datavencimento as data_vencimento,
                        valorprevisto, valorrealizado, realizado, contaativo, nomepessoa, percentualrateio,nomecentrocusto,
                        nomepessoa, observacao, descricao, numeronotafiscal, contaativo, fc.subcategoria4, fc.subcategoria3,
                        fc.subcategoria2, fc.subcategoria, fc.categoria, fc.categoriaprojecao,fc.categoriacustoreceita, conciliadoorigem,
                        conciliadodestino, fc.projeto, fc.produto

                        from {self.schema}.{self.tableName} as fm
                        left join {self.schema}.categories as fc on fc.id = fm.idclassificacao
                        order by data desc, realizado asc"""
            try:
                cur.execute(query=query)
                list_projection: list[Projection] = []
                for row in cur.fetchall():
                    register = Projection(
                    id = row[0],
                    data_liquidação = row[1].date() if type(row[1]) == datetime else None,
                    data_vencimento = row[2].date() if type(row[2]) == datetime else None,
                    valorprevisto = row[3],
                    valorrealizado = row[4],
                    moeda = 'BRL',
                    cotação = 1,
                    valorprevisto_BRL = row[3],
                    valorrealizado_BRL = row[4],
                    realizado = row[5],
                    recorrente = None,
                    de = row[6] if row[3] > 0 else row[7],
                    para = row[7] if row[3] < 0 else row[6],
                    percentualrateio = row[8],
                    nomecentrocusto = row[9] if row[9] != None else "Lumx",
                    nomepessoa = row[10],
                    observacao = row[11],
                    descricao = row[12],
                    numeronotafiscal = row[13],
                    contaativo = row[14],
                    subcategoria4 = row[15],
                    subcategoria3 = row[16],
                    subcategoria2 = row[17],
                    subcategoria = row[18],
                    categoria = row[19],
                    categoriaprojecao = row[20],
                    categoriacusto_receita = row[21],
                    hash = None,
                    check_conciliadoorigem = row[22],
                    check_conciliadodestino = row[23],
                    projeto = row[24],
                    produto = row[25]
                    )
                    list_projection.append(register)
                    
                self.connection.commit()
                return list_projection
            except:
                raise Exception

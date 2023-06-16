import logging
import csv
from io import StringIO
from datetime import datetime
from entities.entityTransaction import TransactionCrypto, Transaction
from entities.entityCoin import Coin
from entities.entityProjection import Projection
from repositories.repositoryBase import RepositoryBase
from repositories.repositoryPrices import RepositoryPrices
import psycopg2

class RepositoryCryptoTransaction ( RepositoryBase ):
    def __init__(self, connection: str, engine: str):
        self.connection: psycopg2.connection = connection
        self.engine = engine
        
        self.schema = 'finance'
        self.tableName = 'movements_crypto'
        self.repositoryPrices = RepositoryPrices(connection,engine)
        super().__init__(connection, engine, self.schema, self.tableName)
        self.transactions: list[Transaction] = []
        
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
                logging.error(e)
                return None

    def deleteByDate(self, date)-> None:
        with self.connection.cursor() as cur:
            try:
                query = f"""delete from {self.schema}.{self.tableName} WHERE date(datetime) = '{date}'"""
                cur.execute(query=query)
                self.connection.commit()
            except:
                raise Exception
    
    def getCryptoTransactions(self) -> list[TransactionCrypto] :
    
        query = f"""
        
        CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
                SELECT
                    subqueryB.time, POWER(c.close, -1) * subqueryB.close AS close, subqueryB.conversionSymbol, subqueryB.date
                FROM
                    {self.repositoryPrices.schema}.{self.repositoryPrices.tableName} AS c
                RIGHT JOIN (
                    SELECT
                        time, close, conversionSymbol, date
                    FROM
                        {self.schema}.{self.repositoryPrices.tableName}
                    ) AS subqueryB ON c.time = subqueryB.time
                WHERE
                    c.conversionsymbol = 'BRL';
            SELECT
                m.id, m.bank, m.methodid, m.datetime,
                m.total, (m.total * pc.close) as totalbrl, m.tokensymbol
            FROM
                {self.schema}.{self.tableName} as m
	            LEFT JOIN {self.schema}.categories as c on m.methodid = c.method_id
            	LEFT JOIN prices as pc on pc.conversionsymbol = m.tokensymbol and date(pc.date) = date(m.datetime)
            ORDER BY
                date desc, tokensymbol asc;"""
    
        try:
            with self.connection.cursor() as cur:
                
                cur.execute(query)
                
                for row in cur.fetchall():
                    transaction = Transaction(
                    id = row[0],
                    idcontaativo = row[1],
                    idclassificacao = row[2],
                    realizado = True,
                    datapagamento = row[3],
                    datavencimento = row[3],
                    valorprevisto = row[4],
                    valorrealizado = row[4],
                    valorprevisto_brl = row[5],
                    valorrealizado_brl = row[5],
                    moeda = row[6]
                    )
                    self.transactions.append(transaction)
            return  self.transactions
        except Exception as e:
            logging.error(e)
                
    def delete_unknown_tokens(self, list_known_tokens: list[Coin]):
        lista_valores = ','.join("'" + str(item) + "'" for item in list_known_tokens)
        with self.connection.cursor() as cur:
            try:
                query = f"""DELETE from {self.schema}.{self.tableName}
                where tokensymbol not in ({lista_valores})
                """
                cur.execute(query=query)
                self.connection.commit()
            except Exception as e:
                logging.error(e)
            
    def getProjection(self) -> list[Projection]:
        with self.connection.cursor() as cur:
             
            query = f"""
            CREATE TEMPORARY TABLE IF NOT EXISTS prices AS
                SELECT
                    subqueryB.time, POWER(c.close, -1) * subqueryB.close AS close, subqueryB.conversionSymbol, subqueryB.date
                FROM
                    {self.schema}.prices_crypto AS c
                RIGHT JOIN (
                    SELECT
                        time, close, conversionSymbol, date
                    FROM
                        {self.schema}.prices_crypto
                    ) AS subqueryB ON c.time = subqueryB.time
                WHERE
                    c.conversionsymbol = 'BRL';
            SELECT
                m.id, m.hash, m.datetime, m.total, m.tokensymbol, pc.close, (m.total * pc.close) as total_BRL,
                b.name as de, b1.name as para, m.bank as contaativo, c.subcategoria4, c.subcategoria3,
                c.subcategoria2, c.subcategoria, c.categoria, c.categoriaprojecao, c.categoriacustoreceita, m.description, c.projeto as c_project, b.project as b_project, b1.project as b1_project, c.produto, c.recorrencia
            FROM
                {self.schema}.{self.tableName} as m
	            LEFT JOIN {self.schema}.categories as c on m.methodid = c.method_id
            	LEFT JOIN {self.schema}.book as b on m.from_ = b.address
            	LEFT JOIN {self.schema}.book as b1 on m.to_ = b1.address
            	LEFT JOIN prices as pc on pc.conversionsymbol = m.tokensymbol and date(pc.date) = date(m.datetime)

            ORDER BY
                date desc, tokensymbol asc;
                
             		;
"""
            try:
                cur.execute(query=query)
                list_projection: list[Projection] = []
                for row in cur.fetchall():
                    register = Projection(
                    id = row[0],
                    data_liquidação = row[2].date() if type(row[2]) == datetime else None,
                    data_vencimento = row[2].date() if type(row[2]) == datetime else None,
                    valorprevisto = row[3],
                    valorrealizado = row[3],
                    moeda = row[4],
                    cotação = row[5],
                    valorprevisto_BRL = row[6],
                    valorrealizado_BRL = row[6],
                    realizado = 1,
                    recorrencia = row[22],
                    de = row[7],
                    para = row[8],
                    percentualrateio = 100,
                    nomecentrocusto = None,
                    nomepessoa = None,
                    observacao = None,
                    descricao = row[17],
                    numeronotafiscal = None,
                    contaativo = row[9],
                    subcategoria4 = row[10],
                    subcategoria3 = row[11],
                    subcategoria2 = row[12],
                    subcategoria = row[13],
                    categoria = row[14],
                    categoriaprojecao = row[15],
                    categoriacusto_receita=row[16],
                    hash = row[1],
                    check_conciliadoorigem = 1,
                    check_conciliadodestino = 1,
                    projeto = row[18] if row[18] != None else row[19] if row[3] > 0 else row[20],
                    produto = row[21]
                    )
                    list_projection.append(register)
                self.connection.commit()
                return list_projection
            except Exception as e:
                logging.error(e)

    def updatebyHash(self, hash, methodid, description) -> None:
        with self.connection.cursor() as cur:
            try:
                query = f"""
                UPDATE
                    {self.schema}.{self.tableName}
                SET
                    methodid = '{methodid}',
                    description = '{description}'
                WHERE
                    hash = '{hash}'
                """
                cur.execute(query=query)
                self.connection.commit()
            except Exception as e:
                logging.error(e)
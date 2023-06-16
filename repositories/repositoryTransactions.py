import psycopg2
import logging
from typing_extensions import Literal
from entities.entityTransaction import Transaction
from repositories.repositoryBase import RepositoryBase
from repositories.repositoryCategories import RepositoryCategories
from repositories.repositoryContacts import RepositoryContacts

class RepositoryTransactions ( RepositoryBase ):
    
    def __init__(self, connection: str, engine: str):
        self.tableName = 'transactions'
        self.schema = 'finance'
        self.connection: psycopg2.connection = connection
        
        self.repositoryCategories = RepositoryCategories(connection, engine)
        self.repositoryContacts = RepositoryContacts(connection, engine)
        
        self.transactions = []
        
        super().__init__(connection, engine, self.schema, self.tableName)

    def insert(self, obj: list[Transaction] | Transaction, method: Literal['bulk', 'single'] = 'bulk') -> None:

        with self.connection.cursor() as cur:
            method = method.lower()
            if method == 'bulk' and type(obj) == list:
                values = [t.to_tuple() for t in obj]
                if not values: return None
                placeholders = ','.join(['%s'] * len(values[0]))
            if method == 'single':
                values = obj.to_tuple()
                placeholders = ','.join(['%s'] * len(values))
            try:
                query = f"""INSERT INTO {self.schema}.{self.tableName}
                
                (id,idexterno,idcontaativo,idclassificacao,realizado,idcentrocusto,tipo,datapagamento,datavencimento,valorprevisto,valorrealizado,valorprevisto_brl,valorrealizado_brl,moeda,descricao,percentualrateio)
                VALUES ({placeholders})
                
                on conflict (id) do update set
                idexterno = EXCLUDED.idexterno,
                idcontaativo = EXCLUDED.idcontaativo,
                idclassificacao = EXCLUDED.idclassificacao,
                realizado = EXCLUDED.realizado,
                idcentrocusto = EXCLUDED.idcentrocusto,
                tipo = EXCLUDED.tipo,
                datapagamento = EXCLUDED.datapagamento,
                datavencimento = EXCLUDED.datavencimento,
                valorprevisto = EXCLUDED.valorprevisto,
                valorrealizado = EXCLUDED.valorrealizado,
                valorprevisto_brl = EXCLUDED.valorprevisto_brl,
                valorrealizado_brl = EXCLUDED.valorrealizado_brl,
                moeda = EXCLUDED.moeda,
                descricao = EXCLUDED.descricao,
                percentualrateio = EXCLUDED.percentualrateio
                ;
                """
                
                cur.executemany(query, values) if method == 'bulk' else cur.execute(query, values)
                self.connection.commit()
            
            except Exception as e:
                logging.error(e)
                print(f'\nNo new transactions found')             
                
    def getTransactions(self) -> list:
        with self.connection.cursor() as cur:
            query = f"""select 
            fm.id,idexterno,idcontaativo,idclassificacao,idcentrocusto,tipo,realizado,datapagamento,datavencimento,valorprevisto,valorrealizado,valorprevisto_brl,valorrealizado_brl,moeda,descricao,percentualrateio,subcategoria4
            from {self.schema}.{self.tableName} as fm
            left join {self.repositoryCategories.schema}.{self.repositoryCategories.tableName} as c on c.id = fm.idclassificacao
            order by fm.datapagamento desc;"""
            
            cur.execute(query)
            result = cur.fetchall()
            self.connection.commit()
            transactions: tuple = []
            for row in result:
                transaction = Transaction(
                    id=row[0],
                    idexterno=row[1],
                    idcontaativo=row[2],
                    idclassificacao=row[3],
                    idcentrocusto=row[4],
                    tipo=row[5],
                    realizado=row[6],
                    datapagamento=row[7],
                    datavencimento=row[8],
                    valorprevisto=row[9],
                    valorrealizado=row[10],
                    valorprevisto_brl=row[11],
                    valorrealizado_brl=row[12],
                    moeda=row[13],
                    descricao=row[14],
                    percentualrateio=row[15],
                )
                subcategoria4 = row[16]
                transactions.append((transaction,subcategoria4))
            
            
        return transactions
    
    def getBalance(self) -> list:
        with self.connection.cursor() as cur:
            query = f"""
            CREATE TEMPORARY TABLE IF NOT EXISTS balance AS (
    SELECT moeda, datapagamento, saldo_local, saldo_brl
    FROM (
        SELECT moeda, datapagamento, SUM(valorrealizado) OVER (PARTITION BY moeda ORDER BY datapagamento) AS saldo_local, SUM(valorrealizado_brl) OVER (PARTITION BY moeda ORDER BY datapagamento) AS saldo_brl,
        ROW_NUMBER() OVER (PARTITION BY moeda, date(datapagamento) ORDER BY datapagamento DESC) AS rn
        FROM {self.schema}.{self.tableName}
        WHERE realizado
    ) AS subquery
    WHERE rn = 1
);

SELECT moeda, MAX(datapagamento) AS close_datetime, saldo_local, saldo_brl
FROM balance
WHERE moeda != 'BRL'
GROUP BY moeda, date(datapagamento), saldo_local, saldo_brl
ORDER BY close_datetime DESC;
    ;"""
            
            cur.execute(query)
            return cur.fetchall()
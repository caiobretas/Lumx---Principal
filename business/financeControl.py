from time import time
from datetime import datetime
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from repositories.repositoryTransactions import RepositoryTransaction
from repositories.repositoryCategories import RepositoryCategories
from repositories.repositoryContacts import RepositoryContacts

from entities.entityContact import Contact
from entities.entityCategory import Category
from entities.entityTransaction import Transaction

class FinanceControl:
    def __init__(self, connection, engine):
        self.repositoryTransaction = RepositoryTransaction(connection, engine)
        self.repositoryContacts = RepositoryContacts(connection, engine)
        self.repositoryCategories = RepositoryCategories(connection, engine)

class Flow(FinanceControl):
    def salaryFlow(self):
        timer = time()
        print('\nUpdating Salary Flow...')
        worksheetid = '1tIf5U3PG5-Lx8p6YxAL9M8jMo2m5PTZX6BS2p2WTp94'
        
        # get the registers from the repository
        query = f'''
        SELECT
		DATE(fm.data) AS data,
    c.subcategoria4,
    hr.nome AS nomepessoa,
    hr.email AS emailpessoa,
    valorprevisto * (-1),
    hr.tipochavepix,
    hr.chavepix,
    fm.numeronotafiscal,
    fm.idkamino
FROM
    {self.repositoryTransaction.schema}.{self.repositoryTransaction.tableName} AS fm
LEFT JOIN
    {self.repositoryTransaction.schema}.{self.repositoryCategories.tableName} AS c ON c.id = fm.idclassificacao
LEFT JOIN
    {self.repositoryContacts.schema}.{self.repositoryContacts.tableName} AS hr ON hr.idpessoa = fm.idpessoa
WHERE
    realizado = 0
    AND
        subcategoria4 in ('Prestação de Serviços','Pró-Labore','Bolsa Auxílio Estágio')
    AND (
        DATE_TRUNC('MONTH', fm.data) = DATE_TRUNC('MONTH', CURRENT_DATE)
        OR DATE_TRUNC('MONTH', fm.data) = DATE_TRUNC('MONTH', CURRENT_DATE)
    )
    AND
        nomepessoa != 'Lumx Studios S/A'
    ORDER BY subcategoria4 desc, nomepessoa asc, valorprevisto desc
'''
        transactions_list = self.repositoryTransaction.runQuery(query)

        # create lists of the values that are going to be written in Google Sheets
        liberados_values_list = []
        aguardandoNFSe_values_list = []
        for transaction in transactions_list:
            transactiondate: datetime = transaction[0].strftime('%m-%Y')
            category = transaction[1]
            contactName = transaction[2]
            contactEmail = transaction[3]
            transationValue = float(transaction[4])
            contactPixKey = transaction[5]
            contactPixKeyType = transaction[6]
            numeronotafiscal = transaction[7]
        
            # ps: the order here influences what's shown in Google Sheets
            if numeronotafiscal != '' or category != 'Prestação de Serviços':
                liberados_values_list.append((transactiondate,category,contactName,contactEmail,transationValue,contactPixKey,contactPixKeyType))
            else:
                aguardandoNFSe_values_list.append((transactiondate,category,contactName,contactEmail,transationValue,contactPixKey,contactPixKeyType))
                
        GoogleSheets().overwriteWorksheet_byID(worksheetid, liberados_values_list, sheetName='Liberados')
        GoogleSheets().overwriteWorksheet_byID(worksheetid, aguardandoNFSe_values_list, sheetName='Aguardando NFSe')
        print('\nSalary Flow updated in {:.2f} seconds\n'.format(time() - timer))
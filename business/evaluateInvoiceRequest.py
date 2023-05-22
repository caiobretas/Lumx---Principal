import logging
from repositories.repositoryTransactions import RepositoryTransaction
from entities.entityEmailRequest import EmailRequest
from senders.InvoiceRequest import InvoiceRequest

class EvaluateInvoiceRequest:
    def __init__(self, connection, engine):
        self.connection = connection
        self.engine = engine
        self.list_requests: list[EmailRequest] = []
    
    def getMissingInvoices(self):
        self.repositoryTransactions = RepositoryTransaction(self.connection, self.engine)
        try:
            query = """
            SELECT
                DATE(fm.data) AS data, idkamino,hr.id, hr.nome AS nomepessoa, hr.email AS emailpessoa, valorprevisto * (-1) as valorprevisto, realizado, fm.id as external_id
            FROM
                finance.movements AS fm
                LEFT JOIN
                    finance.categories AS c ON c.id = fm.idclassificacao
                LEFT JOIN
                    h_resources.contacts AS hr ON hr.idpessoa = fm.idpessoa
            WHERE
                subcategoria4 = 'Prestação de Serviços' 
                AND fm.data > '2023-05-01' AND fm.data < DATE_TRUNC('MONTH', CURRENT_DATE) + INTERVAL '2 month'
	            AND (fm.numeronotafiscal IS NULL OR fm.numeronotafiscal = '')
                AND nomepessoa != 'Lumx Studios S/A'
            ORDER BY
                data asc
                ;"""
            return self.repositoryTransactions.runQuery(query)
        
        except Exception as e:
            logging.error(e)
    
    def createRequests(self) -> list[EmailRequest]:
        for row in self.getMissingInvoices():
            request = EmailRequest(
                external_id = row[7],
                datetime = row[0],
                contact_id= row[2],
                contact_name=row[3],
                to_=row[4],
                )
            InvoiceRequest(request, row[5])
            self.list_requests.append(request)
        return self.list_requests
            
    def updateRequestsTable(self) -> None: # postgresql
        from repositories.repositoryEmailRequests import RepositoryEmailRequests
        RepositoryEmailRequests(self.connection, self.engine).insertEmailRequests(self.list_requests)        
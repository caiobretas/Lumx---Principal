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
                DATE(fm.data) AS data, idkamino,hr.id, hr.nome AS nomepessoa, hr.email AS emailpessoa, valorprevisto * (-1) as valorprevisto, realizado, fm.id as external_id, hr.emailsecundario as emailsecundario
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
    
    def updateRequestsTable(self,list_requests) -> None: # postgresql
        from repositories.repositoryEmailRequests import RepositoryEmailRequests
        RepositoryEmailRequests(self.connection, self.engine).insertEmailRequests(list_requests)  
        
    def createInvoiceRequest(self) -> list[EmailRequest]:
        '''Return the list of invoice requests created'''
        for row in self.getMissingInvoices():
            request = EmailRequest(
                external_id = row[7],
                datetime = row[0],
                contact_id= row[2],
                contact_name=row[3],
                to_=row[4],
                secondaryemail=row[8],
                )
            invoiceRequest = InvoiceRequest(request, row[5])
            emailRequest = EmailRequest(
                external_id=invoiceRequest.KaminoId_transaction,
                draft_id=invoiceRequest.request.draft_id,
                email_id=invoiceRequest.request.email_id,
                datetime=invoiceRequest.request.datetime,
                request_type=invoiceRequest.request.request_type,
                contact_id=invoiceRequest.request.contact_id,
                contact_name=invoiceRequest.request.contact_name,
                from_=invoiceRequest.request.from_,
                to_=invoiceRequest.request.to_,
                subject=invoiceRequest.request.subject
            )
            self.list_requests.append(emailRequest)
        
        #  writes the requests created in the database
        self.updateRequestsTable(self.list_requests)
        return self.list_requests
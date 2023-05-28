import logging
from repositories.repositoryTransactions import RepositoryTransaction
from repositories.repositoryEmailRequests import RepositoryEmailRequests
from entities.entityEmailRequest import EmailRequest
from senders.InvoiceRequest import InvoiceRequest

class EvaluateInvoiceRequest:
    def __init__(self, connection, engine):
        self.connection = connection
        self.engine = engine
        self.list_requests: list[EmailRequest] = []
        self.repositoryTransactions: RepositoryTransaction = RepositoryTransaction(connection, engine)
        self.repositoryEmailRequests: RepositoryEmailRequests = RepositoryEmailRequests(connection, engine)
        
    def updateRequestsTable(self,list_requests) -> None: # postgresql
        from repositories.repositoryEmailRequests import RepositoryEmailRequests
        RepositoryEmailRequests(self.connection, self.engine).insertEmailRequests(list_requests)  
        
    def createInvoiceRequest(self) -> list[EmailRequest]:
        '''Return the list of invoice requests created'''
        for row in self.repositoryTransactions.getMissingInvoices():
            request = EmailRequest(
                external_id = row[7],
                datetime = row[0],
                contact_id= row[2],
                contact_name=row[3],
                to_=row[4],
                secondaryemail=row[8],
                value=row[5]
                )
            invoiceRequest = InvoiceRequest(request)
            
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
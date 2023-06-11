from repositories.repositoryTransactionsKamino import RepositoryKamino
from repositories.repositoryEmailRequests import RepositoryEmailRequests

from entities.entityEmailRequest import EmailRequest
from senders.InvoiceRequest import InvoiceRequest
class EvaluateInvoiceRequest:
    '''Determines whether an invoice is going to be created or reminded'''
    def __init__(self, connection, engine):
        self.connection = connection
        self.engine = engine
        self.list_requests: list[EmailRequest] = []
        self.RepositoryKamino: RepositoryKamino = RepositoryKamino(connection, engine)
        self.repositoryEmailRequests: RepositoryEmailRequests = RepositoryEmailRequests(connection, engine)
        
    def insertIntoEmailsRequestsTable(self,list_requests=None) -> None: # postgresql
        from repositories.repositoryEmailRequests import RepositoryEmailRequests
        if not list_requests: return None
        else: RepositoryEmailRequests(self.connection, self.engine).insertEmailRequests(list_requests)
        
    def sendInvoiceRequest(self) -> list[EmailRequest]:
        '''Return a list of created requests'''
        self.repositoryEmailRequests.getEmailRequests(False,False,'Invoice')
        
        externalIds_list: list = self.repositoryEmailRequests.getExternalIds(request_type='Invoice')
        for row in self.RepositoryKamino.getMissingInvoices():
            request = EmailRequest(
                external_id = row[7],
                datetime = row[0],
                contact_id= row[2],
                contact_name=row[3],
                to_=row[4],
                secondaryemail=row[8],
                value=row[5]
            )
            if request.external_id in externalIds_list: continue # check if the external id already has a request in the repository
            invoiceRequest = InvoiceRequest(request)
            draft = invoiceRequest.setDraft()[0]
            invoiceRequest.sendDraft(draft) # send the invoice request

            emailRequest = EmailRequest(
                external_id=invoiceRequest.request.external_id,
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
        
        self.insertIntoEmailsRequestsTable(self.list_requests) #  writes the requests created in the database
        return self.list_requests

    def sendInvoiceReminder(self) -> list[EmailRequest]:
        '''Send reminder notification and return a list of reminders sent'''
        for request in self.repositoryEmailRequests.getEmailRequests(pendingOnly=True):
            invoiceRequest = InvoiceRequest(request)
            reminder = invoiceRequest.setReminder(request.email_id)
            invoiceRequest.sendReminder(reminder)
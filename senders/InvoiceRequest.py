from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
from datetime import timedelta
class InvoiceRequest:
    
    def setMessage(self) -> tuple:
        self.from_: str = 'financeiro@lumxstudios.com'
        subject = f'NFS-e {self.contactName} - {self.date}'
        message = f'Prezado(a) {self.contactName},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.invoiceValue}\n\nEsta é uma mensagem automática'
        self.request.subject = subject
        return subject, message
   
    def sendMessage(self):
        message: tuple = self.setMessage()
        GoogleGmail().sendMessage(message[0], message[1], self.contactEmail, self.from_)
        
        
    def __init__(self, request: EmailRequest, value):
        self.request = request
        self.datetime = request.datetime
        self.KaminoId_transaction: str = request.external_id
        self.contactId: str = request.contact_id
        self.contactName: str = request.contact_name
        # self.contactEmail: str = request.to_ tirei para fins de teste
        self.contactEmail = 'caio.bretas@lumxstudios.com'
        self.invoiceValue: float = value
        
        self.date = (request.datetime - timedelta(days=30)).strftime('%m/%Y')
    
        request.request_type = 'Invoice'
        request.from_ = self.from_
        request.to_ = self.contactEmail
        
        self.setMessage()
        self.sendMessage()
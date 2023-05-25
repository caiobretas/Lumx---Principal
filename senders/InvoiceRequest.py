from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
from datetime import timedelta, datetime
class InvoiceRequest:
    
    def setDraft(self) -> tuple:
        self.request.subject = f'NFS-e {self.request.contact_name} - {self.date}'
        message = f'Prezado(a) {self.request.contact_name},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.invoiceValue}\n\nEsta é uma mensagem automática'
        draftId = GoogleGmail().createDraft(self.request.from_, self.request.to_, self.cc_list, self.request.subject, message)
        return draftId
    
    def sendDraft(self) -> None:
        self.request.draft_id = self.setDraft()
        self.request.email_id = GoogleGmail().sendDraft(self.request.draft_id)
        return ((self.request.draft_id, self.request.email_id))
        
    def setMessage(self) -> tuple:
        subject = f'NFS-e {self.request.contact_name} - {self.date}'
        message = f'Prezado(a) {self.request.contact_name},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.invoiceValue}\n\nEsta é uma mensagem automática'
        self.request.subject = subject
        return subject, message
        
    def sendMessage(self):
        message: tuple = self.setMessage()
        GoogleGmail().sendMessage(message[0], message[1], self.contactEmail, self.from_)
    
    def __init__(self, request: EmailRequest, value):
        self.request = request
        self.KaminoId_transaction: str = request.external_id
        self.contactEmail: str = request.to_
        self.invoiceValue: float = value
        self.cc_list = [request.secondaryemail, 'financeiro@lumxstudios.com'] if request.secondaryemail != None else [request.to_]

        self.date = (request.datetime - timedelta(days=30)).strftime('%m/%Y')
    
        request.request_type = 'Invoice'
        request.from_ = 'caio.bretas@lumxstudios.com'
        request.datetime = datetime.now()
        
        self.sendDraft()
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
from datetime import timedelta, datetime
class InvoiceRequest:
    
    def setDraft(self) -> tuple:
        self.request.subject = f'NFS-e {self.request.contact_name} - {self.date}'
        message = f'Prezado(a) {self.request.contact_name},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.request.value}\n\nEm caso de dúvidas, envie um e-mail para financeiro@lumxstudios.com\n\nEsta é uma mensagem automática.'
        draft = GoogleGmail().createDraft(self.request.from_, self.request.to_, self.cc_list, self.request.subject, message)
        return draft, draft['id']
    
    def setMessage(self) -> tuple:
        self.request.subject = f'NFS-e {self.request.contact_name} - {self.date}'
        message = f'Prezado(a) {self.request.contact_name},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.request.value}\n\nEm caso de dúvidas, envie um e-mail para financeiro@lumxstudios.com\n\nEsta é uma mensagem automática.'
        return self.request.subject, message
    
    def setReminder(self, messageId=None) -> None:
        if not messageId: return None
        message = f'Olá {self.request.contact_name.split()[0]},\n\nA solicitação ainda está pendente, favor anexar o solicitado.'
        draft = GoogleGmail().createDraft(self.request.from_,self.request.to_, self.cc_list, self.request.subject, message, messageId)
        return draft
        
    def sendDraft(self, draft) -> None:
        self.request.draft_id = draft['id']
        self.request.email_id = GoogleGmail().sendDraft(self.request.draft_id)
        return (self.request.draft_id, self.request.email_id)
        
    def sendMessage(self):
        message: tuple = self.setMessage()
        GoogleGmail().sendMessage(message[0], message[1], self.contactEmail, self.request.from_)
    
    def sendReminder(self, draftReminder):
        self.request.draft_id = draftReminder['id']
        self.request.email_id = GoogleGmail().sendDraft(self.request.draft_id)
        return (self.request.draft_id, self.request.email_id)
        
    def __init__(self, request: EmailRequest):
        self.request = request
        self.contactEmail: str = request.to_
        # self.contactEmail = 'caiodbretas@icloud.com'
        
        self.cc_list = [request.secondaryemail, 'financeiro@lumxstudios.com'] if request.secondaryemail != None else ['financeiro@lumxstudios.com']
        # self.cc_list = ['caio.bretas@lumxstudios.com']
        self.date = (request.datetime - timedelta(days=30)).strftime('%m/%Y')
    
        self.request.request_type = 'Invoice'
        self.request.from_ = 'caio.bretas@lumxstudios.com'
        self.request.datetime = datetime.now()
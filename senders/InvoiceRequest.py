from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
from datetime import timedelta, datetime
class InvoiceRequest:
    
    def setDraft(self) -> tuple:
        self.request.subject = f'NFS-e {self.request.contact_name} - {self.date}'
        message = f'Prezado(a) {self.request.contact_name},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.request.value}\n\nEsta é uma mensagem automática'
        draft = GoogleGmail().createDraft(self.request.from_, self.request.to_, self.cc_list, self.request.subject, message)
        return draft, draft['id']
    
    def setMessage(self) -> tuple:
        self.request.subject = f'NFS-e {self.request.contact_name} - {self.date}'
        message = f'Prezado(a) {self.request.contact_name},\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês {self.date}\n\nValor: R${self.request.value}\n\nEsta é uma mensagem automática'
        return self.request.subject, message
    
    def setReminder(self, draft: dict) -> None:
        draftId = draft.get(draftId, None)
        message_body = f'{self.request.contact_name}, está requisição está pendente.\n\nFavor responder a este e-mail com a Nota Fiscal de Serviços referente ao mês{self.date}\n\nEsta é uma mensagem automática'
        draft['message']['threadId'] = draft.get('thread_id',None)
        draft['message']['payload']['headers'] = [
            {'name': 'In-Reply-To', 'value': draft['message']['id']
        }
    ]
        
    def sendDraft(self) -> None:
        self.request.draft_id = self.setDraft()
        self.request.email_id = GoogleGmail().sendDraft(self.request.draft_id)
        return ((self.request.draft_id, self.request.email_id))
        
    def sendMessage(self):
        message: tuple = self.setMessage()
        GoogleGmail().sendMessage(message[0], message[1], self.contactEmail, self.request.from_)
    
    def __init__(self, request: EmailRequest):
        self.request = request
        self.KaminoId_transaction: str = request.external_id
        self.contactEmail: str = request.to_
        
        self.cc_list = [request.secondaryemail, 'financeiro@lumxstudios.com'] if request.secondaryemail != None else [request.to_]

        self.date = (request.datetime - timedelta(days=30)).strftime('%m/%Y')
    
        self.request.request_type = 'Invoice'
        self.request.from_ = 'caio.bretas@lumxstudios.com'
        self.request.datetime = datetime.now()
        
        self.setDraft()
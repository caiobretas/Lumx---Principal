from main import Main
from business.updateBook import UpdateBook
from business.UpdateContacts import UpdateContacts
from business.updateCategories import UpdateCategories
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateFutures import UpdateFutures
from business.updateKaminoTransactions import UpdateKaminoTransactions
from business.updateTransactionsRepository import UpdateTransactions

from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail


main = Main()
connection = main.connection
engine = main.engine

sender = GoogleGmail()
from_ = 'caio.bretas@lumxstudios.com'
to = 'caiodbretas@icloud.com'
errorsubject = 'Error running script!'
class AutorunMinute: 
    
    list_errors: list[Exception] = []
    
    @staticmethod
    def run():    
        try:
            main.admin()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
            None
        try:
            UpdateCryptoPrices(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
            None
        try:
            UpdateKaminoTransactions(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
            None
        try:
            UpdateFutures(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
            None
        try:
            UpdateContacts(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
            None
        # try:
        #     UpdateTransactions(connection, engine).update()
        # except Exception as e:
        #     draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
        #     AutorunMinute.list_errors.append(e)
        #     None

    def sender():
        subject = 'Successfully completed 10 minute routine'
        message = '\n\nThe following tasks were executed:\nUpdateEmailRequest_Table\nUpdateKaminoTransactions_Table\nUpdateContacts_Table\n'
        sender.createDraft(from_=from_,to=to,subject=subject, message_body=message)
        
AutorunMinute.run()
AutorunMinute.sender()
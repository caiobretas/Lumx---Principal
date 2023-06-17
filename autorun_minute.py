from main import Main
from business.updateBook import UpdateBook
from business.UpdateContacts import UpdateContacts
from business.updateCategories import UpdateCategories
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateFutures import UpdateFutures
from business.updateKaminoTransactions import UpdateKaminoTransactions
from business.updateTransactionsRepository import UpdateTransactions
from business.comercial import PipedriveActivities, PipedriveDeals, PipedriveDealFields

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
            UpdateBook(connection,engine).update()
            UpdateCategories(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
        try:
            main.admin()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
        try:
            UpdateCryptoPrices(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
        try:
            UpdateKaminoTransactions(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
        try:
            UpdateFutures(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)

        try:
            UpdateContacts(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
        
        try:
            PipedriveActivities.PipedriveActivities(connection,engine).update()
            PipedriveDeals.PipedriveDeals(connection,engine).update()
            PipedriveDealFields.PipedriveDealField(connection,engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
    
    @staticmethod
    def sender():
        subject = 'Successfully completed 10 minute routine'
        message = 'The following tasks were executed:\n\nUpdateBook_Table\nUpdateUpdateEmailRequest_Table\nUpdateKaminoTransactions_Table\nUpdateContacts_Table'
        draft: dict = sender.createDraft(from_=from_,to=to,subject=subject, message_body=message)
        sender.sendDraft(draft.get('id', None))
        
AutorunMinute.run()
AutorunMinute.sender()
print('Auto Run Minute Complete')
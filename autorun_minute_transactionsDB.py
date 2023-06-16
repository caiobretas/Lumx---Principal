from main import Main
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
            UpdateTransactions(connection, engine).update()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunMinute.list_errors.append(e)
            
    @staticmethod
    def sender():
        subject = 'Successfully completed transactions update routine'
        message = 'The following tasks were executed:\n\nUpdateTransactions_Table'
        draft: dict = sender.createDraft(from_=from_,to=to,subject=subject, message_body=message)
        sender.sendDraft(draft.get('id', None))
        
AutorunMinute.run()
AutorunMinute.sender()
print('Auto Run Minute Complete')
from main import Main
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail


main = Main()
connection = main.connection
engine = main.engine

sender = GoogleGmail()
from_ = 'caio.bretas@lumxstudios.com'
to = 'caiodbretas@icloud.com'
errorsubject = 'Error running script!'
# class AutorunDay: 
    
#     list_errors: list[Exception] = []
    
#     @staticmethod
#     def run():    
#         try:
#             main.emailrequests()
#         except Exception as e:
#             draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
#             sender.sendDraft(draft.get('id', None))
#             AutorunDay.list_errors.append(e)
            
#     @staticmethod
#     def sender():
#         subject = 'Successfully completed hour routine'
#         message = 'The following tasks were executed:\nInvoiceRequest\nReminderRequest'
#         draft: dict = sender.createDraft(from_=from_,to=to,subject=subject, message_body=message)
#         sender.sendDraft(draft.get('id', None))
        
# AutorunDay.run()
# AutorunDay.sender()
# print('Auto Run Day Complete')


# main.flows()
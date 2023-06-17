from main import Main
from business.updateProjection import UpdateProjection
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from business.finance.ExchangeVariationRate import ExchangeVariationRate
from business.finance.ExchangeVariationRate import ExchangeVariationRate

main = Main()
connection = main.connection
engine = main.engine

sender = GoogleGmail()
from_ = 'caio.bretas@lumxstudios.com'
to = 'caiodbretas@icloud.com'
errorsubject = 'Error running script!'
class AutorunHour: 
    
    list_errors: list[Exception] = []
    
    @staticmethod
    def run():    
        try:
            UpdateProjection(connection, engine).update()
            ExchangeVariationRate(connection, engine).updateSheet()
        except Exception as e:
            draft: dict = sender.createDraft(from_=from_,to=to,subject=errorsubject,message_body=f'Error: {e}')
            sender.sendDraft(draft.get('id', None))
            AutorunHour.list_errors.append(e)
            
    @staticmethod
    def sender():
        subject = 'Successfully completed hour routine'
        message = 'The following tasks were executed:\n\nUpdateProjection_Sheet'
        draft: dict = sender.createDraft(from_=from_,to=to,subject=subject, message_body=message)
        sender.sendDraft(draft.get('id', None))
        
AutorunHour.run()
AutorunHour.sender()
print('Auto Run Hour Complete')


main.flows()
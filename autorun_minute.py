from main import Main
from business.updateBook import UpdateBook
from business.UpdateContacts import UpdateContacts
from business.updateCategories import UpdateCategories
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateFutures import UpdateFutures
from business.updateKaminoTransactions import UpdateKaminoTransactions
from business.updateTransactionsRepository import UpdateTransactions

from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail

sender = GoogleGmail
main = Main()
connection = main.connection
engine = main.engine

from_ = 'caio.bretas@lumxstudios.com'
to_ = 'caiodbretas@icloud.com'
subject = 'Error running script!'


try:
    main.admin()
except Exception as e:
    sender.createDraft(from_=from_,to_=to_,subject=subject,message_body=f'Error: {e}')
    None
try:
    UpdateCryptoPrices(connection, engine).update()
except Exception as e:
    sender.createDraft(from_=from_,to_=to_,subject=subject,message_body=f'Error: {e}')
    None
try:
    UpdateKaminoTransactions(connection, engine).update()
except Exception as e:
    sender.createDraft(from_=from_,to_=to_,subject=subject,message_body=f'Error: {e}')
    None
try:
    UpdateFutures(connection, engine).update()
except Exception as e:
    sender.createDraft(from_=from_,to_=to_,subject=subject,message_body=f'Error: {e}')
    None
try:
    UpdateContacts(connection, engine).update()
except Exception as e:
    sender.createDraft(from_=from_,to_=to_,subject=subject,message_body=f'Error: {e}')
    None
try:
    UpdateTransactions(connection, engine).update()
except Exception as e:
    sender.createDraft(from_=from_,to_=to_,subject=subject,message_body=f'Error: {e}')
    None
    
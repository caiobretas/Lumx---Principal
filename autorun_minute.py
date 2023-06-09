from main import Main
from business.updateBook import UpdateBook
from business.UpdateContacts import UpdateContacts
from business.updateCategories import UpdateCategories
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateFutures import UpdateFutures
from business.updateKaminoTransactions import UpdateKaminoTransactions
from business.updateTransactionsRepository import UpdateTransactions

main = Main()
connection = main.connection
engine = main.engine

UpdateCryptoPrices(connection, engine).update()
UpdateKaminoTransactions(connection, engine).update()
UpdateTransactions(connection, engine).update()
UpdateFutures(connection, engine).update()
UpdateContacts(connection, engine).update()

main.admin()
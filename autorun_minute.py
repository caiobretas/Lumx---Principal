from main import Main
from business.updateBook import UpdateBook
from business.updateContacts import UpdateContacts
from business.updateCategories import UpdateCategories
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateFutures import UpdateFutures

from business.updateTransactionsRepository import UpdateTransactions

main = Main()
connection = main.connection
engine = main.engine

UpdateFutures(connection, engine).update()
UpdateBook(connection, engine).update()
UpdateContacts(connection, engine).update()
UpdateCategories(connection, engine).update()
UpdateCryptoPrices(connection, engine).update()
UpdateTransactions(connection, engine).update()


main.admin()
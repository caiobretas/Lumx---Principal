from main import Main
from business.updateBook import UpdateBook
from business.UpdateContacts import UpdateContacts
from business.updateCategories import UpdateCategories


main = Main()
connection = main.connection
engine = main.engine

UpdateBook(connection, engine).update()
UpdateContacts(connection, engine).update()
UpdateCategories(connection, engine).update()
main.admin()
main.flows()
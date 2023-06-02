from main import Main
from business.updateFutures import UpdateFutures
from business.updateCryptoTransactions  import UpdateCryptoTransactions
from business.updateProjection import UpdateProjection

main = Main()
connection = main.connection
engine = main.engine

UpdateFutures(connection, engine).update()
UpdateCryptoTransactions(connection, engine).update()
UpdateProjection(connection, engine).update()
main.flows()
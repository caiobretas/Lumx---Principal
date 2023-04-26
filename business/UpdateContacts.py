from controllers.controllerHTTP.controllerKamino import ControllerKamino
from repositories.repositoryContacts import RepositoryContacts

class UpdateContacts:
    def __init__(self, connection, engine, schema, tableName) -> None:
        self.repositoryContacts = RepositoryContacts(connection, engine, schema, tableName)
        self.repositoryContacts.insertContacts(ControllerKamino().getContacts())
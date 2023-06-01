from controllers.controllerHTTP.controllerKamino import ControllerKamino
from repositories.repositoryContacts import RepositoryContacts

class UpdateContacts:
    def __init__(self, connection, engine) -> None:
        self.connection = connection
        self.engine = engine
    
    def update(self):
        self.repositoryContacts = RepositoryContacts(self.connection, self.engine)
        self.repositoryContacts.insertContacts(ControllerKamino().getContacts())        
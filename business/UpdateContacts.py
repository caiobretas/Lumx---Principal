from controllers.controllerHTTP.controllerKamino import ControllerKamino
from repositories.repositoryContacts import RepositoryContacts

class UpdateContacts:
    def __init__(self, connection, engine) -> None:
        self.repositoryContacts = RepositoryContacts(connection, engine)
        self.repositoryContacts.insertContacts(ControllerKamino().getContacts())
        
        # apagar linha 9 e 10
        # q = 1
        
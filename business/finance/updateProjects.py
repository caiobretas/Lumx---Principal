from repositories.repositoryProjects import RepositoryProjects
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets

class UpdateProjects:
    def __init__(self, connection, engine):
        self.repositoryProjects = RepositoryProjects(connection,engine)
        
    def update(self):
        projects = self.repositoryProjects.getProjects_fromSheets()
        self.repositoryProjects.insert(projects)
        a = 1
        
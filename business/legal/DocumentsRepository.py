from repositories.legal.repositoryDocuments import RepositoryDocuments
from controllers.controllerGoogle.controllerGoogleDrive import GoogleDrive
from entities.legal.entityDocument import Document


class DocumentsRepository:
    
    def __init__(self, connection, engine):
        
        self.controllerDrive = GoogleDrive()
        self.repositoryDocuments = RepositoryDocuments(connection, engine)

    def update(self):
        
        self.controllerDrive.getFilesByDriveId(self.repositoryDocuments.driveId, driveName='Jurídico')
        files: list[Document] = self.controllerDrive.files
        
        self.repositoryDocuments.insertDocuments(files)
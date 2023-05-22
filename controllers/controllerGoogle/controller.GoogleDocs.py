from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
import logging
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
class GoogleDocs(ControllerGoogle):
    
    def __init__(self):
        try:
            super().__init__()
            self.service = build('docs','v1', credentials=self.credential)
        except HttpError as err:
            print(err)
            
    def getDocument_data(self, id):
        # Retrieve the documents contents from the Docs service.
        try:
            # document = self.service.documents().get(documentId=documentID).execute()
            # print('The title of the document is: {}'.format(document.get('title')))
            document = self.service.documents().get(documentId=id).execute()
            document_id = document.get('documentId')
            document_title = document.get('title')
            return document_id, document_title
        except Exception as e:
            logging.error(e)
            
    def createDocument(self, title=None):
        '''create a new document and return the id and title'''
        try:
            document = self.service.documents().create(
                body={
                    'title': title,
                    }
            ).execute()
            return document.get('documentId'), title
        except Exception as e:
            logging.error(e)
            return None
    
    def updateDocument(self, id, requests: list[dict]):
        try:
            return self.service.documents().batchUpdate(
                documentId=id,
                body={'requests': requests}
            ).execute()
    
        except Exception as e:
            logging.error(e)
            return None
    
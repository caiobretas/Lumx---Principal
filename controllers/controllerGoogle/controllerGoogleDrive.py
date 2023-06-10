from io import BytesIO
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.errors import HttpError
import logging
from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
from googleapiclient.discovery import build, Resource

class GoogleDrive (ControllerGoogle):
    def __init__ (self):
        try:
            super().__init__()
            self.service: Resource = build('drive', 'v3', credentials=self.credential)
        except Exception as e:
            logging.error(e)
            
    def getSharedDrives(self) -> list[dict]:
        'return a list of shared drives'
        return self.service.drives().list().execute()
    
    def deleteSharedDrives(self,driveId):    
        try:
           self.service.drives().delete(driveId=driveId).execute()
        except Exception as e:
            logging.error(e)
            
    def createFolder(self, name, parentId=None):
        """Create and return a folder.

        Param: parentId is used for sharedDrives as well.
        """ 
        folder_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parentId] if parentId else []
        }
        try:
            folder = self.service.files().create(body=folder_metadata,supportsAllDrives=True).execute()
            return folder
        except HttpError as err:
            logging.error(err)
    
    def uploadFile(self,file_bytes,file_name,folder_id):
        
        file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
        media = MediaIoBaseUpload(BytesIO(file_bytes), mimetype='application/octet-stream')
        
        try:
            return self.service.files().create(body=file_metadata, media_body=media, supportsAllDrives=True).execute()
        except HttpError as e:
            logging.error(e)
            return None
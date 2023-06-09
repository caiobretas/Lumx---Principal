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
            
    def getSharedDrives(self):
        drives = self.service.drives().list().execute()
        print(drives)
    
    def deleteSharedDrives(self,driveId):    
        try:
           self.service.drives().delete(driveId=driveId).execute()
        except Exception as e:
            logging.error(e)
            
    def createFolder(self, name, parentId=None, sharedDriveId=None):
        folder_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parentId]
        }
        # if parentId:
        #     folder_metadata['parents'] = [parentId]
        #     if sharedDriveId: folder_metadata['parents'].append(sharedDriveId)
        # if not parentId:
        #     if sharedDriveId: folder_metadata['parents'] = [sharedDriveId]
        
        folder = self.service.files().create(body=folder_metadata).execute()
        return folder
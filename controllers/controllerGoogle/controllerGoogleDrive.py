import logging
from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
from googleapiclient.discovery import build, Resource

class ControllerDrive (ControllerGoogle):
    def __init__ (self):
        try:
            super().__init__()
            self.service: Resource = build('drive', 'v3', credentials=self.credential)
        except Exception as e:
            logging.error(e)

    def getArchive(self):
        
import logging
from controllers.controllerPipeDrive.controllerPipeDrive import ControllerPipeDrive
from repositories.comercial.repositoryPipedriveActivities import RepositoryPipedriveActivites
from entities.comercial.entityPipedriveActivity import PipedriveActivity

class PipedriveActivities:
    def __init__(self, connection, engine):
        self.controllerPipe = ControllerPipeDrive()
        self.repositoryActivities = RepositoryPipedriveActivites(connection, engine)
    
    def update(self):
        try:
            activities: list[PipedriveActivity] = self.controllerPipe.getActivities()
            self.repositoryActivities.insert(activities)
        except Exception as e:
            logging.error(e)
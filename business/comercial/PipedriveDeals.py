import logging
from controllers.controllerPipeDrive.controllerPipeDrive import ControllerPipeDrive
from repositories.comercial.repositoryPipedriveDeals import RepositoryPipedriveDeals
from repositories.comercial.repositoryPipedriveActivities import RepositoryPipedriveActivites
from entities.comercial.entityPipedriveDeal import PipedriveDeal
from entities.comercial.entityPipedriveActivity import PipedriveActivity
class PipedriveDeals:
    def __init__(self, connection, engine):
        self.controllerPipe = ControllerPipeDrive()
        self.repositoryDeals = RepositoryPipedriveDeals(connection, engine)
        self.repositoryActivities = RepositoryPipedriveActivites(connection, engine)
    
    def update(self):
        try:
            deals_list = self.controllerPipe.getDeals()
            self.repositoryDeals.insert(deals_list)
        except Exception as e:
            logging.error(e)
            
    def getActivities(self):
        try:
            activities: list[PipedriveActivity] = self.controllerPipe.getActivities()
            self.repositoryActivities.insert(activities)
        except Exception as e:
            logging.error(e)
            
    def getFlow(self) -> list:
        'não está pronto'
        try:
            deals: list[PipedriveDeal] = self.controllerPipe.getDeals()
            flows
            for deal in deals:
                flows: list = self.controllerPipe.getFlowbyDealId(deal.id)['data']
                
        except Exception as e:
            logging.error(e)
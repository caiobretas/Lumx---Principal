import logging
from controllers.controllerPipeDrive.controllerPipeDrive import ControllerPipeDrive
from repositories.comercial.repositoryPipedriveDeals import RepositoryPipedriveDeals
from entities.comercial.entityPipedriveDeal import PipedriveDeal
class PipedriveDeals:
    def __init__(self, connection, engine):
        self.controllerPipe = ControllerPipeDrive()
        self.repositoryDeals = RepositoryPipedriveDeals(connection, engine)
    
    def update(self):
        try:
            deals_list = self.controllerPipe.getDeals()
            self.repositoryDeals.insert(deals_list)
        except Exception as e:
            logging.error(e)
    
    def getFlow(self) -> list:
        try:
            deals: list[PipedriveDeal] = self.controllerPipe.getDeals()
            flows
            for deal in deals:
                flows: list = self.controllerPipe.getFlowbyDealId(deal.id)['data']
                
        except Exception as e:
            logging.error(e)
import logging
from controllers.controllerPipeDrive.controllerPipeDrive import ControllerPipeDrive
from repositories.comercial.repositoryPipedriveDealFieldOptions import RepositoryPipedriveDealFieldOptions
from repositories.comercial.repositoryPipedriveDealFields import RepositoryPipedriveDealFields

class PipedriveDealField:
    def __init__(self, connection, engine):
        self.controllerPipe = ControllerPipeDrive()
        self.repositoryDealFieldOptions = RepositoryPipedriveDealFieldOptions(connection, engine)
        self.repositoryDealFields = RepositoryPipedriveDealFields(connection,engine)
    
    def update(self):
        try:
            fieldsAndoptions_tuple = self.controllerPipe.getDealsFields()
            dealFields =fieldsAndoptions_tuple[0]
            dealOptions = fieldsAndoptions_tuple[1]
             
        except Exception as e:
            logging.error(e)
        try:
            self.repositoryDealFields.insert(dealFields)
            self.repositoryDealFieldOptions.insert(dealOptions)
        except Exception as e:
            logging.error(e)
            
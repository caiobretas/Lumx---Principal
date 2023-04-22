from time import time

from controllers.controllerProtocol.controllerVolume import ControllerVolume

from controllers.controllerFinance.controllerPrices import ControllerPrices
from controllers.controllerFinance.controllerControle import ControllerControle
from controllers.controllerFinance.controllerPrices import ControllerPrices

from entities.entityVolume import Volume, VolumeWallets
from entities.entityCoin import Coin
from entities.entityControle import Controle

from repositories.repositoryVolume import RepositoryVolume
from repositories.repositoryWallets import RepositoryWallets
from repositories.repositoryControle import RepositoryControle


class GetRepositoryData:
    def __init__(self, connFinance, engineAdmin) -> None:
        self.start_time = time()
        
        self.finance_controllerPrices = ControllerPrices(connFinance, schema='finance', tableName='prices_crypto')
        self.finance_controllerControle = ControllerControle(connFinance)
        self.finance_prices = ControllerVolume(connFinance)
        
        self.repositoryWallets = RepositoryWallets(connection=connFinance, engine=engineAdmin, schema='finance', tableName='projects_wallets')
        self.repositoryControle = RepositoryControle(connection=connFinance, engine=engineAdmin, schema='finance', tableName=None)
        self.repositoryVolume = RepositoryVolume(connection=connFinance, engine=engineAdmin, schema='finance', tableName=None)

        self.lst_coinPrices: list[Coin] = self.finance_controllerPrices.getPrices()
        self.lst_volumes: list[Volume] = self.repositoryVolume.getVolume()
        self.lst_volumesWallets: list[VolumeWallets] = self.repositoryWallets.getVolumeWallets()
        self.lst_controle: list[Controle] = self.repositoryControle.getControle()

        print('\nRepository data loaded in {:.2f} seconds\n'.format(time() - self.start_time))
from time import time

from controllers.controllerProtocol.controllerBlockchains import ControllerBlockchain
from controllers.controllerProtocol.controllerCollections import ControllerCollections
from controllers.controllerProtocol.controllerUser import ControllerUsers
from controllers.controllerProtocol.controllerWallets import ControllerWallets
from controllers.controllerProtocol.controllerMintRequests import ControllerMintRequests
from controllers.controllerProtocol.controllerProjects import ControllerProjects
from controllers.controllerProtocol.controllerVolume import ControllerVolume

from entities.entityBlockchain import Blockchain
from entities.entityCollection import Collection
from entities.entityUser import User
from entities.protocol.entityWallet import Wallet
from entities.entityMintRequest import MintRequest
from entities.entityProject import Project
from entities.entityVolume import Volume, VolumeWallets
from entities.entityBillings import Billing

from interfaces.interfaceBillings import InterfaceBillings

class GetProtocolData:

    def __init__(self, pathIF, conn: str) -> None:
        timer = time()
        
        self.pathIF = pathIF

        self.connectionProtocol = conn

        self.protocol_controllerBlockchains = ControllerBlockchain(self.connectionProtocol)
        self.protocol_controllerCollections = ControllerCollections(self.connectionProtocol)
        self.protocol_controllerMintRequests = ControllerMintRequests(self.connectionProtocol)
        self.protocol_controllerUser = ControllerUsers(self.connectionProtocol)
        self.protocol_controllerWallets = ControllerWallets(self.connectionProtocol)
        self.protocol_controllerProjects = ControllerProjects(self.connectionProtocol)
        self.protocol_controllerVolumes = ControllerVolume(self.connectionProtocol)

        self.interfaceBillings = InterfaceBillings(path=self.pathIF, sheetName='Interface Cobranças')

        self.lst_billings: list[Billing] = self.interfaceBillings.get_Billings()
        self.lst_blockchains: list[Blockchain] = self.protocol_controllerBlockchains.getBlockchain()
        self.lst_collections: list[Collection] = self.protocol_controllerCollections.get_Collections()
        self.lst_mintRequests: list[User] = self.protocol_controllerMintRequests.get_mintRequests()
        self.lst_users: list[Wallet] = self.protocol_controllerUser.get_User()
        self.lst_wallets: list[MintRequest] = self.protocol_controllerWallets.get_Wallets()
        self.lst_projects: list[Project] = self.protocol_controllerProjects.get_Projects()
        self.lst_volume: list[Volume] = self.protocol_controllerVolumes.get_Volumes()
        self.lst_Wallets: list[VolumeWallets] = self.protocol_controllerVolumes.get_VolumeWallets()
        
        print('\nProtocol data loaded in {:.2f} seconds\n'.format(time() - timer))
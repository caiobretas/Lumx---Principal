from time import time

from repositories.repositoryVolume import RepositoryVolume
from repositories.repositoryProjects import RepositoryProjects
from repositories.repositoryBillings import RepositoryBillings
from repositories.repositoryCategories import RepositoryCategories

from business.getProtocoldata import GetProtocolData
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateCategories import UpdateCategories
from business.updateTransactions import UpdateTransactions
from business.updateCryptoTransactions import UpdateCryptoTransactions
from business.updateFutures import UpdateFutures
from business.updateBook import UpdateBook

from business.assembleProjection import AssembleProjection

class AtualizaFinanceRepository:
    def __init__(self, connFinance, engine, schema, pathIF, connProtocol) -> None:
        timer = time()

        # self.protocolData = GetProtocolData(pathIF=pathIF, conn=connProtocol)

        # self.repositoryProjects = RepositoryProjects(connection=connFinance, engine=engine, schema=schema, tableName='projects')
        # self.repositoryVolume = RepositoryVolume(connection=connFinance, engine=engine, schema=schema, tableName='projects_volumes')
        # self.repositoryVolumeWallets = RepositoryVolume(connection=connFinance, engine=engine, schema=schema, tableName='projects_wallets')
        # self.repositoryBillings = RepositoryBillings(connection=connFinance, engine=engine, schema=schema, tableName='projects_billings')

        # self.repositoryProjects.insereProjeto(self.protocolData.lst_projects)
        # self.repositoryVolume.insereVolume(self.protocolData.lst_volume)
        # self.repositoryVolumeWallets.insereVolumeWallets(self.protocolData.lst_Wallets)
        # self.repositoryBillings.insertBilling(self.protocolData.lst_billings)

        UpdateBook(connection=connFinance, engine=engine, schema=schema, tableName='book', path_interface=pathIF,sheetName_interface='book')
        UpdateCryptoTransactions(connection=connFinance, engine=engine, schema='finance', tableName='movements_crypto')
        # UpdateCryptoPrices(connectionFinance=connFinance, engineAdmin=engine, schema=schema, tableName='prices_crypto')
        # UpdateCategories(connection=connFinance, engine=engine,pathIF=pathIF,schema='finance', sheetName='categories', tableName='categories')
        # UpdateTransactions(connection=connFinance,engine=engine,schema='finance',tableName='movements')
        # UpdateFutures(connection=connFinance,engine=engine,schema='finance',tableName='movements')

        # AssembleProjection(connection=connFinance,engine=engine,schema='finance',tableName='movements').getRegisters()
        
        print('\nDatabase updated in {:.2f} seconds\n'.format(time() - timer))

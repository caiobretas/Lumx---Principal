from time import time

from viewers.viewerVolumes import ViewerVolumes
from viewers.viewerProjects import ViewerProjects
from viewers.viewerBillings import ViewerBillings
from viewers.viewerPrices import ViewerPrices
from viewers.viewerControle import ViewerControle

from business.calculaVolume import CalculaVolume
from business.tiraCurrency import TiraCurrency
from business.preencheControle import PreencheControle

from business.getProtocoldata import GetProtocolData
from business.getRepositoryData import GetRepositoryData

from business.writeMovements import WriteTranscations
from business.writeProjection import WriteProjection

# this instance is used to update all the viewers
class AtualizaViewer:
    def __init__(self, pathVW, pathIF, connProtocol, connFinance, engineAdmin, schema) -> None:
        timer = time()
        
        # self.viewerBillings = ViewerBillings(path=pathVW, sheetName  = 'Tabela Cobranças')
        # self.viewerPrices = ViewerPrices(path=pathVW, sheetName = 'Tabela Cotações')
        # self.viewerProjects = ViewerProjects(path=pathVW, sheetName = 'Tabela Projetos')
        # self.viewerVolumes = ViewerVolumes(path=pathVW, sheetName = 'Tabela Volumes')
        # self.viewerVolumeWallets = ViewerVolumes(path=pathVW, sheetName = 'Tabela Wallets')
        # self.viewerControle = ViewerControle(path=pathVW, sheetName = 'Controle')

        # self.repositoryData = GetRepositoryData(connFinance=connFinance, engineAdmin=engineAdmin)
        # self.protocolData = GetProtocolData(pathIF=pathIF, conn=connProtocol)

        # print('\nRepository data loaded in {:.2f} seconds\n'.format(time() - timer))
    
        # timer = time()

        # TiraCurrency(self.repositoryData.lst_volumes)
        # CalculaVolume.calculaVolume(lst=self.repositoryData.lst_volumes)
        # CalculaVolume.calculaVolumeBRL(lst=self.repositoryData.lst_volumes)
        # # falta otimizar
        # PreencheControle(path=pathVW,lst=self.repositoryData.lst_controle, connection=connFinance, engine=engineAdmin, schema=schema).preencheControle()
        
        # print('\nBusiness rules executed in {:.2f} seconds\n'.format(time() - timer))

        # timer = time()

        # self.viewerPrices.insertViewerPrices(lst=self.repositoryData.lst_coinPrices)
        # self.viewerBillings.insertViewerBilling(lst=self.protocolData.lst_billings)
        # self.viewerProjects.insertViewerProject(lst=self.protocolData.lst_projects)
        # self.viewerVolumes.insertViewerVolumes(lst=self.repositoryData.lst_volumes)
        # self.viewerVolumeWallets.insertViewerVolumeWallets(lst=self.repositoryData.lst_volumesWallets)
        # self.viewerControle.insertViewerControle(lst=self.repositoryData.lst_controle)
        
        # writes the transactions
        WriteProjection(connection=connFinance,engine=engineAdmin,schema=schema,path=pathVW,sheetName='Tabela Projeção', tableName='movements')
        # WriteTranscations(connection=connFinance,engine=engineAdmin,schema=schema,path=pathVW,sheetName='Movimentação', tableName='movements')

        print('\nViewer updated in {:.2f} seconds\n'.format(time() - timer))
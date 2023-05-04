from time import time
from viewers.viewerPrices import ViewerPrices
from business.writePrices import WritePrices
from business.writeProjection import WriteProjection

class UpdateProjection(object):
    def __init__(self, pathProjection, connProtocol, connFinance, engineAdmin, schema) -> None:
        timer = time()
        
        WritePrices(path=pathProjection, sheetName = 'Tabela Cotações', connection=connFinance, engine=engineAdmin, schema=schema, tableName='prices_crypto').writePrices()
        WriteProjection(path=pathProjection, connection=connFinance, engine=engineAdmin, schema=schema).insert_projectionTable(sheetName='Tabela Projeção')
        
        print('\Projection updated in {:.2f} seconds\n'.format(time() - timer))
        
        
        
        
        # from viewers.viewerControle import ViewerControle        

        # from viewers.viewerVolumes import ViewerVolumes
        # from viewers.viewerProjects import ViewerProjects
        # from viewers.viewerBillings import ViewerBillings
        
        

        # from business.calculaVolume import CalculaVolume
        # from business.tiraCurrency import TiraCurrency
        # from business.preencheControle import PreencheControle

        # from business.getProtocoldata import GetProtocolData
        # from business.getRepositoryData import GetRepositoryData

        # from business.writeMovements import WriteTranscations

        
        
        # self.viewerBillings = ViewerBillings(path=pathVW, sheetName  = 'Tabela Cobranças')
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

        # self.viewerBillings.insertViewerBilling(lst=self.protocolData.lst_billings)
        # self.viewerProjects.insertViewerProject(lst=self.protocolData.lst_projects)
        # self.viewerVolumes.insertViewerVolumes(lst=self.repositoryData.lst_volumes)
        # self.viewerVolumeWallets.insertViewerVolumeWallets(lst=self.repositoryData.lst_volumesWallets)
        # self.viewerControle.insertViewerControle(lst=self.repositoryData.lst_controle)
        
        # writes the transactions
        # WritePrices()
        
        # WriteTranscations(connection=connFinance,engine=engineAdmin,schema=schema,path=pathVW,sheetName='Movimentação', tableName='movements')
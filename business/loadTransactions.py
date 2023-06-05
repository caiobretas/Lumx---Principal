from time import sleep
from controllers.controllerHTTP.controllerKamino import ControllerKamino
from controllers.controllerHTTP.controllerEtherscan import ControllerEtherscan
from controllers.controllerHTTP.controllerPolygonscan import ControllerPolygonscan
from entities.entityTransaction import Transaction, TransactionCrypto

class LoadTransactions:
    def __init__(self, periodoDe=None, periodoAte=None, apenasRealizados=False):
        self.controllerKamino = ControllerKamino()
        self.periodoDe = periodoDe
        self.periodoAte = periodoAte
        self.apenasRealizados = apenasRealizados
    
    def loadKaminoTransactions(self) -> list[Transaction]:
        try:
            return ControllerKamino().getTransactions(periodoDe=self.periodoDe, periodoAte=self.periodoAte, apenasRealizados=self.apenasRealizados)
      
        except Exception as e:
            print(f'Error: {e}.\n\nperiodoDe e periodoAte não podem ser None\nperiodoDe = {self.periodoDe}\nperiodoAte = {self.periodoAte}')
            raise e
        
    def loadCryptoTransactions(self, is_safe: bool, address, name: str = 'Unknown', chain: str='ethereum') -> list[TransactionCrypto]:
        list_total = []
        
        if is_safe == False or (chain.upper() if chain != None else chain) == 'ETHEREUM':
            list_normal = ControllerEtherscan().get_normalTransactions(name=name,address=address,apiKey='DUUV82YWBS4YIWEURM8V7N5AXWB5ZMJH3A')
            list_internal = ControllerEtherscan().get_internalTransactions(name=name,address=address,apiKey='9W72CXUYN7TSKD29FTRBFB8CFT3I7RRQ1G')
            list_erc20 = ControllerEtherscan().get_erc20Transactions(name,address=address,apiKey='3T8X64FG67EW3MFFWQ5UQYNUMIWBRVG4S4')
            
            list_total.extend(list_normal)
            list_total.extend(list_internal)
            list_total.extend(list_erc20)
            
        if is_safe == False or (chain.upper() if chain != None else chain) == 'POLYGON':
            list_normal = ControllerPolygonscan().get_normalTransactions(name=name,address=address, apiKey='C2KGG1M5CP9QHJH4K183BJQZ611H6EM9CP')
            list_internal = ControllerPolygonscan().get_internalTransactions(name=name,address=address, apiKey='UQMSW9NT6T8IPXWW264RSTKBE872B4HE7N')
            list_erc20 = ControllerPolygonscan().get_erc20Transactions(name=name,address=address, apiKey='UQMSW9NT6T8IPXWW264RSTKBE872B4HE7N')
            
            list_total.extend(list_normal)
            list_total.extend(list_internal)
            list_total.extend(list_erc20)
        return list_total
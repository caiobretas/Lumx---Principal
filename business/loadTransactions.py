from controllers.controllerHTTP.controllerKamino import ControllerKamino
from controllers.controllerHTTP.controllerEtherscan import ControllerEtherscan
from controllers.controllerHTTP.controllerPolygonscan import ControllerPolygonscan
from entities.entityTransaction import Transaction, TransactionCrypto

class LoadTransactions:
    def __init__(self, periodoDe=None, periodoAte=None, apenasRealizados=False):
        self.controllerKamino = ControllerKamino()
        self.contollerEtherscan = ControllerEtherscan()
        self.periodoDe = periodoDe
        self.periodoAte = periodoAte
        self.apenasRealizados = apenasRealizados

    def loadTransactions(self) -> list[Transaction]:
        try:
            return self.controllerKamino.getTransactions(periodoDe=self.periodoDe, periodoAte=self.periodoAte, apenasRealizados=self.apenasRealizados)
       
        except Exception as e:
            print(f'Error: {e}.\n\nperiodoDe e periodoAte não podem ser None\nperiodoDe = {self.periodoDe}\nperiodoAte = {self.periodoAte}')
            raise e
        
    def loadCryptoTransactions(self, metamask: bool, address, apiKey, name = 'Unknown', chain: str='ETH') -> list[TransactionCrypto]:
        list_total = []
        if chain.upper() == 'ETH' or metamask:
            apiKey = 'DUUV82YWBS4YIWEURM8V7N5AXWB5ZMJH3A'
            list_normal = ControllerEtherscan().get_normalTransactions(name=name,address=address,apiKey=apiKey)
            list_internal = ControllerEtherscan().get_internalTransactions(name=name,address=address,apiKey=apiKey)
            list_erc20 = ControllerEtherscan().get_erc20Transactions(name=name,address=address,apiKey=apiKey)
            
            list_total.extend(list_normal)
            list_total.extend(list_internal)
            list_total.extend(list_erc20)
     
        if chain.upper() == 'MATIC' or metamask:
            apiKey = 'V7J58GX39IDM5AQW3XQ8CX98N9E2GFGIKF'
            list_normal = ControllerPolygonscan().get_normalTransactions(name=name,address=address, apiKey=apiKey)
            list_internal = ControllerPolygonscan().get_internalTransactions(name=name,address=address, apiKey=apiKey)
            list_erc20 = ControllerPolygonscan().get_erc20Transactions(name=name,address=address, apiKey=apiKey)

            list_total.extend(list_normal)
            list_total.extend(list_internal)
            list_total.extend(list_erc20)
        return list_total

from time import time
from controllers.controllerHTTP.controllerCryptoCompare import ControllerHTTPPrices
from entities.entityCoin import Coin

class LoadPrices:
    def __init__(self, apiKey_CryptoCompare):
        self.list_Coins = ['USDT', 'USDC', 'ETH', 'MATIC', 'WETH', 'BRL']
        self.apiKey_CryptoCompare = apiKey_CryptoCompare

    def loadPrices(self) -> list[Coin]:
        timer = time()
        self.list_historical: list[Coin] = []
        for coin in self.list_Coins:
            controller_http_prices = ControllerHTTPPrices()
            list_aux = controller_http_prices.get_historical_CoinPrice(tokenSymbol=coin, limit='2000', tsym='USD', apiKey_CryptoCompare=self.apiKey_CryptoCompare)
            self.list_historical.extend(list_aux)
        return self.list_historical
from entities.entityCoin import Coin

from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase

class ControllerHTTPPrices ( ControllerHTTPBase ):

    def get_historical_CoinPrice(self,tokenSymbol: str, limit, tsym, apiKey_CryptoCompare: str=None):
        url_Inicial: str = 'https://min-api.cryptocompare.com/data/v2/histoday'
        fsym: str = tokenSymbol.upper()
        limit: int = limit
        endpoint = f'{url_Inicial}?fsym={fsym}&tsym={tsym}&limit={limit}&toTs=-1&api_key={apiKey_CryptoCompare}'

        try:
            historical_tokenprice = super().runAPI_GET(endpoint=endpoint)

            list_historical : list[Coin] = []
            for dict in historical_tokenprice:
                dict = Coin(
                    id = None,
                    time = dict['time'],
                    high = dict['high'],
                    low = dict['low'],
                    open = dict['open'],
                    volumefrom = dict['volumefrom'],
                    volumeto = dict['volumeto'],
                    close = float((dict['close'])),
                    conversiontype = dict['conversionType'],
                    conversionsymbol = str(tokenSymbol)
                )
               
                list_historical.append(dict)

            
        except Exception as err:
            print(f'\nErro ao puxar preços históricos: {tokenSymbol}')
            raise err

        return list_historical

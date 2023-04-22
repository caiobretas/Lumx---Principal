import datetime
from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase
from entities.entityTransaction import TransactionCrypto

class ControllerEtherscan(ControllerHTTPBase):
    def __init__ (self):
        self.baseUrl = 'https://api.etherscan.io/api'
    
    def get_normalTransactions(self, name, module: str = 'account', action: str ='txlist', address: not None = '<string>', startblock: int = 0, endblock: int = 99999999, page: int=1, sort: str = 'asc', apiKey: not None = '<string>') -> list[TransactionCrypto]:
        try: 
            filtros = f'?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={page}&offset={10000}&sort={sort}&apikey={apiKey}'
            endpoint = self.baseUrl + filtros
            result = super().get(endpoint=endpoint)['result']

            list_Transactions: list[TransactionCrypto] = []
            for dict in result:
                obj = TransactionCrypto(
                blockNumber = dict['blockNumber'], 
                blockHash = dict['blockHash'], 
                timeStamp = int(dict['timeStamp']),
                hash = dict['hash'], 
                nonce = dict['nonce'],
                from_ = dict['from'],
                contractAddress = dict['contractAddress'],
                to = dict['to'],
                gas = dict['gas'],
                gasPrice = dict['gasPrice'],
                gasUsed = dict['gasUsed'],
                cumulativeGasUsed = dict['cumulativeGasUsed'],
                value = int(dict['value']),
                tokenName = 'Ethereum',
                tokenSymbol = 'ETH',
                tokenDecimal = 18,
                isError = int(dict['isError']),
                txreceipt_status = int(dict['txreceipt_status']),
                methodId = dict['methodId'],
                functionName = dict['functionName'],
                txnType ='Normal',
                address=address,
                blockchain='ETH',
                name = name
                )
                list_Transactions.append(obj)
            
            return list_Transactions
            
        except Exception as e:
            raise e
        
    def get_internalTransactions(self, name, module: str = 'account', action: str = 'txlistinternal', address: not None | str = '<string>', startblock: int = 0, endblock: int = 99999999, page: int = 1, offset: str = 10000, sort: str = 'asc', apiKey: not None | str = '<string>') -> list[TransactionCrypto]:
        try:
            filtros = f'?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={apiKey}'
            endpoint = self.baseUrl + filtros
            result = super().get(endpoint=endpoint)['result']

            list_internalTransactions: list[TransactionCrypto] = []
            for dict in result:
                obj = TransactionCrypto(
                blockNumber = dict['blockNumber'],
                timeStamp = int(dict['timeStamp']),
                hash = dict['hash'],
                from_ = dict['from'],
                contractAddress = dict['contractAddress'],
                to = dict['to'],
                gas = dict['gas'],
                gasUsed = dict['gasUsed'],
                value = int(dict['value']),
                tokenName = 'Ehereum',
                tokenSymbol = 'ETH',
                tokenDecimal = 18,
                isError = dict['isError'],
                type = dict['type'],
                txnType = 'Internal',
                address = address,
                name = name,
                blockchain = 'ETH'
                )
                list_internalTransactions.append(obj)
            
            return list_internalTransactions
        
        except Exception as e:
            raise e
        
    def get_erc20Transactions(self, name, module: str = 'account', action: str = 'tokentx', address: not None | str = '<string>', startblock: int = 0, endblock: int = 99999999, page: int = 1, offset: str = 10000, sort: str = 'asc', apiKey: not None | str = '<string>') -> list[TransactionCrypto]:
        try:
            filtros = f'?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={apiKey}'
            endpoint = self.baseUrl + filtros
            result = super().get(endpoint=endpoint)['result']

            list_internalTransactions: list[TransactionCrypto] = []
            for dict in result:
                obj = TransactionCrypto(
                    blockNumber = dict['blockNumber'],
                    blockHash = dict['blockHash'],
                    timeStamp = int(dict['timeStamp']),
                    hash = dict['hash'],
                    nonce = dict['nonce'],
                    from_ = dict['from'],
                    contractAddress = dict['contractAddress'],
                    to = dict['to'],
                    gas = dict['gas'],
                    gasPrice = dict['gasPrice'],
                    gasUsed = dict['gasUsed'],
                    cumulativeGasUsed = dict['cumulativeGasUsed'],
                    value = int(dict['value']),
                    tokenName = dict['tokenName'],
                    tokenSymbol = dict['tokenSymbol'],
                    tokenDecimal = dict['tokenDecimal'],
                    txnType = 'ERC-20',
                    address = address,
                    name = name,
                    blockchain = 'ETH'
                )
                list_internalTransactions.append(obj)
            
            return list_internalTransactions
        
        except Exception as e:
            raise e
import logging
import datetime
from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase
from entities.entityTransaction import TransactionCrypto
import requests

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
                transaction = TransactionCrypto(
                blockNumber = int(dict['blockNumber']), 
                blockHash = str(dict['blockHash']).lower(),
                timeStamp = int(dict['timeStamp']),
                hash = str(dict['hash']).lower(), 
                nonce = int(dict['nonce']),
                from_ = str(dict['from']).lower(),
                contractAddress = str(dict['contractAddress']).lower(),
                to = str(dict['to']).lower(),
                gas = float(dict['gas']),
                gasPrice = float(dict['gasPrice']),
                gasUsed = float(dict['gasUsed']),
                cumulativeGasUsed = float(dict['cumulativeGasUsed']),
                value = float(dict['value']),
                tokenName = 'Ethereum',
                tokenSymbol = 'ETH',
                tokenDecimal = 18,
                isError = int(dict['isError']),
                txreceipt_status = int(dict['txreceipt_status']),
                methodId = dict['methodId'],
                functionName = dict['functionName'],
                txnType ='Normal',
                address=str(address).lower(),
                blockchain='ETH',
                name = str(name),
                scan = 'https://etherscan.io'
                )
                list_Transactions.append(transaction)
            
            return list_Transactions
            
        except Exception as e:
            logging.error(e)
        
    def get_internalTransactions(self, name, module: str = 'account', action: str = 'txlistinternal', address: not None | str = '<string>', startblock: int = 0, endblock: int = 99999999, page: int = 1, offset: str = 10000, sort: str = 'asc', apiKey: not None | str = '<string>') -> list[TransactionCrypto]:
        try:
            filtros = f'?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={apiKey}'
            endpoint = self.baseUrl + filtros
            result = super().get(endpoint=endpoint)['result']

            list_internalTransactions: list[TransactionCrypto] = []
            for dict in result:
                transaction = TransactionCrypto(
                blockNumber = int(dict['blockNumber']),
                timeStamp = int(dict['timeStamp']),
                hash = str(dict['hash']).lower(),
                from_ = str(dict['from']).lower(),
                contractAddress = str(dict['contractAddress']).lower(),
                to = str(dict['to']).lower(),
                gas = float(dict['gas']),
                gasUsed = float(dict['gasUsed']),
                value = float(dict['value']),
                tokenName = 'Ehereum',
                tokenSymbol = 'ETH',
                tokenDecimal = 18,
                txreceipt_status = 1,
                isError = int(dict['isError']),
                type = str(dict['type']).lower(),
                txnType = 'Internal',
                address = str(address).lower(),
                name = str(name),
                blockchain = 'ETH',
                scan = 'https://etherscan.io'
                )
                list_internalTransactions.append(transaction)
            return list_internalTransactions
        
        except Exception as e:
            logging.error(e)
        
    def get_erc20Transactions(self, name, module: str = 'account', action: str = 'tokentx', address: not None | str = '<string>', startblock: int = 0, endblock: int = 99999999, page: int = 1, offset: str = 10000, sort: str = 'asc', apiKey: not None | str = '<string>') -> list[TransactionCrypto]:
        try:
            filtros = f'?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={apiKey}'
            endpoint = self.baseUrl + filtros
            result = super().get(endpoint=endpoint)['result']

            list_erc20Transactions: list[TransactionCrypto] = []
            for dict in result:
                transaction = TransactionCrypto(
                    blockNumber = int(dict['blockNumber']),
                    blockHash = str(dict['blockHash']).lower(),
                    timeStamp = int(dict['timeStamp']),
                    hash = str(dict['hash']).lower(),
                    nonce = int(dict['nonce']),
                    from_ = str(dict['from']).lower(),
                    contractAddress = str(dict['contractAddress']).lower(),
                    to = str(dict['to']).lower(),
                    gas = float(dict['gas']),
                    gasPrice = float(dict['gasPrice']),
                    gasUsed = float(dict['gasUsed']),
                    cumulativeGasUsed = float(dict['cumulativeGasUsed']),
                    value = float(dict['value']),
                    tokenName = str(dict['tokenName']),
                    tokenSymbol = str(dict['tokenSymbol']).upper(),
                    tokenDecimal = int(dict['tokenDecimal']),
                    isError = 0,
                    txreceipt_status = 1,
                    txnType = 'ERC-20',
                    address = str(address).lower(),
                    name = str(name),
                    blockchain = 'ETH',
                    scan = 'https://etherscan.io'
                )
                list_erc20Transactions.append(transaction)
            
            return list_erc20Transactions
        
        except Exception as e:
            logging.error(e) 
from uuid import UUID, uuid4
from datetime import datetime
import pytz

class Transaction:
    def __init__(self, id, tipo, data, datapagamento, datavencimento, datacompetencia, valorprevisto, valorrealizado, percentualrateio, realizado, idcontaorigem, nomecontaorigem, codigoreduzidoorigem, idcontadestino , nomecontadestino, codigoreduzidodestino, idcentrocusto , nomecentrocusto, idpessoa , nomepessoa, observacao, cpfcnpjpessoa, descricao, idunidadenegocio, nomeunidadenegocio, numeronotafiscal, conciliadoorigem, conciliadodestino, saldoiniciodiacontaativo, saldofimdiaccontaativo, idprojeto, nomeprojeto, nomeclassificacao, contaativo):
        
        self.id = id
        self.tipo = tipo
        self.data = data
        self.datapagamento = datapagamento
        self.datavencimento = datavencimento
        self.datacompetencia = datacompetencia
        self.valorprevisto = valorprevisto
        self.valorrealizado = valorrealizado
        self.percentualrateio = percentualrateio
        self.realizado = realizado
        self.idcontaorigem = idcontaorigem
        self.nomecontaorigem = nomecontaorigem
        self.codigoreduzidoorigem = codigoreduzidoorigem
        self.idcontadestino = idcontadestino
        self.nomecontadestino = nomecontadestino
        self.codigoreduzidodestino = codigoreduzidodestino
        self.idcentrocusto = idcentrocusto
        self.nomecentrocusto = nomecentrocusto
        self.idpessoa = idpessoa
        self.nomepessoa = nomepessoa
        self.observacao = observacao
        self.cpfcnpjpessoa = cpfcnpjpessoa
        self.descricao = descricao
        self.idunidadenegocio = idunidadenegocio
        self.nomeunidadenegocio = nomeunidadenegocio
        self.numeronotafiscal = numeronotafiscal
        self.conciliadoorigem = conciliadoorigem
        self.conciliadodestino = conciliadodestino
        self.saldoiniciodiacontaativo = saldoiniciodiacontaativo
        self.saldofimdiaccontaativo = saldofimdiaccontaativo
        self.idprojeto = idprojeto
        self.nomeprojeto = nomeprojeto
        self.nomeclassificacao = nomeclassificacao
        self.contaativo = contaativo

        if self.tipo == 'Pagamento':
            self.valorprevisto = (-1) * valorprevisto if valorprevisto != None else None
            self.valorrealizado = (-1) * valorrealizado if valorrealizado != None else None
            self.nomecontadestino = nomepessoa
            self.nomecontaorigem = contaativo

        if self.tipo == 'Recebimento':
            self.nomecontadestino = contaativo
            self.nomecontaorigem = nomepessoa

        
    def to_tuple(self) -> tuple:
        return (self.id, self.tipo, self.data, self.datapagamento, self.datavencimento, self.datacompetencia, self.valorprevisto, self.valorrealizado, self.percentualrateio, self.realizado, self.idcontaorigem, self.nomecontaorigem, self.codigoreduzidoorigem, self.idcontadestino , self.nomecontadestino, self.codigoreduzidodestino, self.idcentrocusto , self.nomecentrocusto, self.idpessoa , self.nomepessoa, self.observacao, self.cpfcnpjpessoa, self.descricao, self.idunidadenegocio, self.nomeunidadenegocio, self.numeronotafiscal, self.conciliadoorigem, self.conciliadodestino, self.saldoiniciodiacontaativo, self.saldofimdiaccontaativo, self.idprojeto, self.nomeprojeto, self.nomeclassificacao, self.contaativo)
     
    def __repr__(self) -> str:
        return f'\nID = {self.id}\n'

class TransactionCrypto:
    def __init__(self,
    blockNumber = None,
    blockHash = None,
    timeStamp = None,
    hash = None,
    nonce = None,
    from_: str = None,
    contractAddress = None,
    to: str = None,
    gas = None,
    gasPrice = None,
    gasUsed = None,
    cumulativeGasUsed = None,
    value = None,
    gasFee = None,
    total = None,
    tokenName = None,
    tokenSymbol = None,
    tokenDecimal = None,
    isError = None,
    txreceipt_status = None,
    type = None,
    methodId = None,
    functionName = None,
    txnType = None,
    address: str=None,
    blockchain=None,
    name: str=None,
    scan: str=None
    ):
        
        self.id = str(uuid4())
        self.blockNumber = blockNumber
        self.blockHash = blockHash
        self.datetime = datetime.fromtimestamp(timeStamp)
        self.hash = hash
        self.nonce = nonce
        self.from_ = from_.lower()
        self.to_ = to.lower()
        self.contractAddress = contractAddress
        self.gas: float = gas
        self.gasPrice: float = (gasPrice / (10**18)) if gasPrice != None else gasPrice
        self.gasUsed: float = gasUsed
        self.cumulativeGasUsed: float = cumulativeGasUsed
        self.value = (value / (10**float(tokenDecimal)))
        self.gasFee = gasFee
        self.total = total
        self.tokenName = tokenName
        self.tokenSymbol = tokenSymbol
        self.tokenDecimal = int(tokenDecimal)
        self.isError = isError
        self.txreceipt_status: int = txreceipt_status
        self.type = type
        self.methodId = methodId
        self.functionName = functionName
        self.txnType: str = txnType
        self.address = address.lower()
        self.blockchain = blockchain
        self.name = name
        self.scan = scan + f'/tx/{self.hash}'
        
        if self.address == self.from_:
            self.value = (value / (10**int(tokenDecimal))) * (-1)
        
        if self.isError != 0:
            self.txreceipt_status = 0
            self.value = 0



    def to_tuple(self) -> tuple:
        return (self.id, self.blockNumber,self.blockHash,self.datetime,self.hash,self.nonce,self.from_,self.to_,self.contractAddress,self.gas,self.gasPrice,self.gasUsed,self.cumulativeGasUsed,self.value,self.gasFee,self.total,self.tokenName,self.tokenSymbol,self.tokenDecimal,self.isError,self.txreceipt_status,self.type,self.methodId,self.functionName,self.txnType, self.blockchain, self.address, self.name, self.scan)
     
    def __repr__(self) -> str:
        return f'Bank: {self.name} - Type: {self.txnType} - Chain: {self.blockchain} - Symbol: {self.tokenSymbol} - Datetime: {self.datetime}'
    
    def __str__(self) -> str:
        return f'Transação {self.txnType} - ID: {self.id}'
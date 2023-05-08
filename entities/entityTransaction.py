from uuid import uuid4
from datetime import datetime, timedelta

class Transaction:
    def __init__(self,id=None,idKamino=None, tipo=None, data=None, datapagamento=None, datavencimento=None, datacompetencia=None, valorprevisto=None, valorrealizado=None, percentualrateio=None, realizado=None, idcontaorigem=None, nomecontaorigem=None, codigoreduzidoorigem=None, idcontadestino =None, nomecontadestino=None, codigoreduzidodestino=None, idcentrocusto =None, nomecentrocusto=None, idpessoa =None, nomepessoa=None, observacao=None, cpfcnpjpessoa=None, descricao=None, idunidadenegocio=None, nomeunidadenegocio=None, numeronotafiscal=None, conciliadoorigem=None, conciliadodestino=None, saldoiniciodiacontaativo=None, saldofimdiaccontaativo=None, idprojeto=None, nomeprojeto=None, nomeclassificacao=None, contaativo=None):
        self.id = str(uuid4()) if id == None else id
        self.idKamino = idKamino
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
        return (self.id, self.tipo, self.data, self.datapagamento, self.datavencimento, self.datacompetencia, self.valorprevisto, self.valorrealizado, self.percentualrateio, self.realizado, self.idcontaorigem, self.nomecontaorigem, self.codigoreduzidoorigem, self.idcontadestino , self.nomecontadestino, self.codigoreduzidodestino, self.idcentrocusto , self.nomecentrocusto, self.idpessoa , self.nomepessoa, self.observacao, self.cpfcnpjpessoa, self.descricao, self.idunidadenegocio, self.nomeunidadenegocio, self.numeronotafiscal, self.conciliadoorigem, self.conciliadodestino, self.saldoiniciodiacontaativo, self.saldofimdiaccontaativo, self.idprojeto, self.nomeprojeto, self.nomeclassificacao, self.contaativo, self.idKamino)
     
    def __repr__(self) -> str:
        return f'ID = {self.id}\n'

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
    gas = 0,
    gasPrice = 0,
    gasUsed = 0,
    cumulativeGasUsed = None,
    value = None,
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
    scan: str=None,
    description: str=None,
    ):
        
        self.id = str(uuid4())
        self.blockNumber = blockNumber
        self.blockHash = blockHash
        self.datetime = datetime.fromtimestamp(timeStamp) + timedelta(hours=3)
        self.hash = hash
        self.nonce = nonce
        self.from_ = str(from_).strip().lower()
        self.to_ = str(to).strip().lower()
        self.contractAddress = contractAddress
        self.gas: float = gas
        self.gasPrice: float = (gasPrice / (10**float(tokenDecimal))) * (-1)
        self.gasUsed: float = gasUsed if str(address).lower() == str(from_).lower() else 0
        self.cumulativeGasUsed: float = cumulativeGasUsed
        self.value = 0 if (txreceipt_status == 0) else ((value / (10**float(tokenDecimal))) * (-1) if str(address).lower() == str(from_).lower() else (value / (10**int(tokenDecimal))))
        self.gasFee = 0 if (str(txnType).strip().lower() == 'erc-20' or str(txnType).strip().lower() == 'Internal') else ((self.gasUsed * self.gasPrice))
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
        self.description = description
        self.scan = scan + f'/tx/{self.hash}'
        
        self.txreceipt_status = 0 if (self.isError != 0 and self.isError != None) else 1
        
        self.total = self.value + self.gasFee
        
        self.methodId = '0xa9059cbb' if (str(txnType) == 'ERC-20' or str(txnType) == 'Internal') else methodId


    def to_tuple(self) -> tuple:
        return (self.id, self.blockNumber,self.blockHash,self.datetime,self.hash,self.nonce,self.from_,self.to_,self.contractAddress,self.gas,self.gasPrice,self.gasUsed,self.cumulativeGasUsed,self.value,self.gasFee,self.total,self.tokenName,self.tokenSymbol,self.tokenDecimal,self.isError,self.txreceipt_status,self.type,self.methodId,self.functionName,self.txnType, self.blockchain, self.address, self.name, self.scan, self.description)
     
    def __repr__(self) -> str:
        return f'Bank: {self.name} - Type: {self.txnType} - Chain: {self.blockchain} - Symbol: {self.tokenSymbol} - Datetime: {self.datetime}'
    
    def __str__(self) -> str:
        return f'Transação {self.txnType} - ID: {self.id}'
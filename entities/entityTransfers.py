from entities.entityContaOrigem import ContaOrigem

class Transfer:
    def __init__(self, id, data, descricao,valor, idContaOrigem, nomeContaOrigem, hierarquia_contaOrigem, tipo_contaOrigem,idContaDestino,nomeContaDestino,contaDestino,idUsuarioInclusao,usuarioInclusao,dataHoraInclusao,idExtratoBancoOrigem,idConciliacaoBancariaOrigem,idExtratoBancoDestino,idConciliacaoBancariaDestino):
        
        self.id = int(id)
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.idContaOrigem = idContaOrigem
        self.nomeContaOrigem = nomeContaOrigem
        self.contaOrigem = ContaOrigem(id=idContaOrigem, name=nomeContaOrigem, hierarchy=hierarquia_contaOrigem, type=tipo_contaOrigem)
        self.idContaDestino = idContaDestino
        self.nomeContaDestino = nomeContaDestino
        self.contaDestino = contaDestino
        self.idUsuarioInclusao = idUsuarioInclusao
        self.usuarioInclusao = usuarioInclusao
        self.dataHoraInclusao = dataHoraInclusao
        self.idExtratoBancoOrigem = idExtratoBancoOrigem
        self.idConciliacaoBancariaOrigem = idConciliacaoBancariaOrigem
        self.idExtratoBancoDestino = idExtratoBancoDestino
        self.idConciliacaoBancariaDestino = idConciliacaoBancariaDestino


    def __str__(self) -> str:
        return f'\nID Transferência: {self.id}\nConta: {self.contaOrigem}\nConta Destino: {self.contaDestino}\nUsuário: {self.usuarioInclusao}\n'
    
    def __repr__(self) -> str:
        return f'\nID Transferência: {self.id}\nConta: {self.contaOrigem}\nConta Destino: {self.contaDestino}\nUsuário: {self.usuarioInclusao}\n'
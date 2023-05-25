from uuid import uuid4
class Contact:
    def __init__(self,ID: str = None,Nome: str = None,CPFCNPJ: str = None,NomeFantasia: str = None,Logradouro: str = None,Nro: str = None,Complemento: str = None,Bairro: str = None,CEP: str = None,Cidade: str = None,UF: str = None,NomePais: str = None,Ativo: str = None,Email: str = None,Telefone: str = None,Cliente: str = None,Fornecedor: str = None,Sexo: str = None,RG: str = None,OrgaoEmissorRG: str = None,UFEmissorRG: str = None,CodigoBanco: str = None,NomeBanco: str = None,AgenciaBancaria: str = None,DigitoAgenciaBancaria: str = None,ContaBancaria: str = None,DigitoContaBancaria: str = None,TipoContaBancaria: str = None, ClienteDesde: str = None,IDClassificacaoPreferencial: str = None,IDCentroCustoPreferencial: str = None, Observacoes: str = None,ChavePix: str = None,TipoChavePix: str = None, EmailSecundario: str = None):
        self.id = str(uuid4())
        self.idpessoa = ID
        self.nome = Nome
        self.cpfcnpj = CPFCNPJ
        self.nomefantasia = NomeFantasia
        self.logradouro = Logradouro
        self.nro = Nro
        self.complemento = Complemento
        self.bairro = Bairro
        self.cep = CEP
        self.cidade = Cidade
        self.uf = UF
        self.nomepais = NomePais
        self.ativo = Ativo
        self.email = Email
        self.telefone = Telefone
        self.cliente = Cliente
        self.fornecedor = Fornecedor
        self.sexo = Sexo
        self.rg = RG
        self.orgaoemissorrg = OrgaoEmissorRG
        self.ufemissorrg = UFEmissorRG
        self.clientedesde = ClienteDesde
        self.idclassificacaopreferencial = IDClassificacaoPreferencial
        self.idcentrocustopreferencial = IDCentroCustoPreferencial
        self.observacoes = Observacoes
        self.chavepix = ChavePix
        self.tipochavepix = TipoChavePix
        self.emailsecundario = EmailSecundario

    def __repr__(self):
        return f'Contact'

    def to_tuple(self) -> tuple:
        return (self.id,self.idpessoa,self.nome,self.cpfcnpj,self.nomefantasia,self.logradouro,self.nro,self.complemento,self.bairro,self.cep,self.cidade,self.uf,self.nomepais,self.ativo,self.email,self.telefone,self.cliente,self.fornecedor,self.sexo,self.rg,self.orgaoemissorrg,self.ufemissorrg,self.clientedesde,self.idclassificacaopreferencial,self.idcentrocustopreferencial,self.observacoes,self.chavepix,self.tipochavepix, self.emailsecundario)
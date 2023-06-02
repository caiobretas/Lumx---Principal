import uuid
import datetime
import logging

from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase
from entities.entityTransfers import Transfer
from entities.entityTransaction import Transaction
from entities.entityContact import Contact

class ControllerKamino ( ControllerHTTPBase ):
    def __init__ (self):
        self.baseUrl = 'https://lumxstudios.kamino.tech'

        accept = 'application/json'
        app='51d32727-39b0-429f-ae38-02dc3068382f'
        cn='LumxStudios8473'
        idUsr='6'
        hash='RUCCQkFHQUc6QkqAPjpEQUqFOn6EQkk6PkGCgUI+RklCSUGFgEZ+PkSCPoI6RYI+STpEgX5KOoA+gkk6fkRCRkI+gUZAhD5GjZmOnJaXmYKJkZZJREdCRg=='
        usr='b6a04d0d-5d08-4ca9-b0d8-a43630c61e06'
    
        self.headers = {'Accept': accept,
                        'App': app,
                        'CN': cn,
                        'IDUsr': idUsr,
                        'Hash': hash,
                        'Usr': usr}

    def postTransfer(self, dict_: Transfer):
        url = '/api/financeiro/transferencia'
        endpoint = self.baseUrl + url

        super().post(endpoint=endpoint, dict_=dict_, headers=self.headers)

    def getTransfers(self, id: int = None, period_from: datetime.datetime =None, period_to: datetime.datetime=None) -> list[Transfer]:
        try:
            url = '/api/financeiro/transferencia/lista'
            
            filtros = f'?filtro.iD={id}&filtro.periodoDe={period_from}&filtro.periodoAte={period_to}'

            endpoint = self.baseUrl + url + filtros
            
            list_aux: list[dict] = []
            for dict_ in super().get(endpoint=endpoint, headers=self.headers):
                dict_ = Transfer(
                idKamino = dict_['ID'],
                data  = dict_['Data'],
                descricao = dict_['Descricao'],
                valor = dict_['Valor'],
                idContaOrigem = dict_['IDContaOrigem'],
                nomeContaOrigem = dict_['NomeContaOrigem'],
                hierarquia_contaOrigem = dict_['ContaOrigem']['Hierarquia'],
                tipo_contaOrigem = dict_['ContaOrigem']['Tipo'],
                idContaDestino = dict_['IDContaDestino'],
                nomeContaDestino = dict_['NomeContaDestino'],
                contaDestino = dict_['ContaDestino'],
                idUsuarioInclusao = dict_['IDUsuarioInclusao'],
                usuarioInclusao = dict_['UsuarioInclusao'],
                dataHoraInclusao = dict_['DataHoraInclusao'],
                idExtratoBancoOrigem = dict_['IDExtratoBancoOrigem'],
                idConciliacaoBancariaOrigem = dict_['IDConciliacaoBancariaOrigem'],
                idExtratoBancoDestino = dict_['IDExtratoBancoDestino'],
                idConciliacaoBancariaDestino = dict_['IDConciliacaoBancariaDestino'])
                list_aux.append(dict_)

            return list_aux
        
        except Exception as e:
            print(f'\nErr: {e}\n')
            raise e
    
    def getTransactions(self, periodoDe: datetime.datetime = '<datetime>',periodoAte: datetime.datetime = '<datetime>',competenciaDe:datetime.datetime = '<datetime>',competenciaAte:datetime.datetime = '<datetime>',apenasRealizados: bool = False,incluirRateio: bool = True,guidFormato: uuid.UUID = '<uuid>',idBanco: int = '<integer>',separador: int = '<integer>' ,tipoArquivo: str = 'JSON',removerCabecalho: bool = False):
        
        try: 
            url = '/api/exportacao/financeiro'
            filtros = f'?periodoDe={periodoDe}&periodoAte={periodoAte}&competenciaDe={competenciaDe}&competenciaAte={competenciaAte}&apenasRealizados={apenasRealizados}&incluirRateio={incluirRateio}&guidFormato={guidFormato}&idBanco={idBanco}&separador={separador}&tipoArquivo={tipoArquivo}&removerCabecalho={removerCabecalho}'
            endpoint = self.baseUrl + url + filtros
            
            self.futures: list[Transaction] = []
            list_aux: list[Transaction] = []
            for row in super().get(type='CSV', endpoint=endpoint, headers=self.headers):
                obj: Transaction = Transaction(
                idKamino = row['ID'],
                tipo = row['Tipo'],
                data = datetime.datetime.strptime(row['Data'],'%d/%m/%Y').date(),
                datapagamento = datetime.datetime.strptime(row['DataPagamento'],'%d/%m/%Y').date() if row['DataPagamento'] != '' else None,
                datavencimento = datetime.datetime.strptime(row['DataVencimento'],'%d/%m/%Y').date(),
                datacompetencia = datetime.datetime.strptime(row['DataCompetencia'],'%d/%m/%Y').date(),
                valorprevisto = float(str(row['ValorPrevisto']).replace(',','.')),
                valorrealizado = float(str(row['ValorRealizado']).replace(',','.')) if row['ValorRealizado'] != '' else None,
                percentualrateio = float(str(row['PercentualRateio']).replace(',','.')) if row['PercentualRateio'] != '' else None,
                realizado = int(row['Realizado']) if row['Realizado'] != '' else None,
                idcontaorigem = int(row['IDContaOrigem']) if row['IDContaOrigem'] != '' else None,
                nomecontaorigem = row['NomeContaOrigem'],
                codigoreduzidoorigem = row['CodigoReduzidoOrigem'],
                idcontadestino  = int(row['IDContaDestino']) if row['IDContaDestino'] != '' else None,
                nomecontadestino = row['NomeContaDestino'],
                codigoreduzidodestino = row['CodigoReduzidoDestino'],
                idcentrocusto = int(row['IDCentroCusto']) if row['IDCentroCusto'] != '' else None,
                nomecentrocusto = row['NomeCentroCusto'],
                idpessoa = int(row['IDPessoa']) if row['IDPessoa'] != '' else None,
                nomepessoa = row['NomePessoa'],
                observacao = row['Observacao'],
                cpfcnpjpessoa = row['CPFCNPJPessoa'],
                descricao = row['Descricao'],
                idunidadenegocio = int(row['IDUnidadeNegocio']) if row['IDUnidadeNegocio'] != '' else None,
                nomeunidadenegocio = row['NomeUnidadeNegocio'],
                numeronotafiscal = row['NumeroNotaFiscal'],
                conciliadoorigem = row['ConciliadoOrigem'],
                conciliadodestino = row['ConciliadoDestino'],
                saldoiniciodiacontaativo = row['SaldoInicioDiaContaAtivo'] if row['SaldoInicioDiaContaAtivo'] != '' else 0,
                saldofimdiaccontaativo = row['SaldoFimDiaContaAtivo'] if row['SaldoFimDiaContaAtivo'] != '' else 0,
                idprojeto = int(row['IDProjeto']) if row['IDProjeto'] != '' else None,
                nomeprojeto = row['NomeProjeto'],
                nomeclassificacao = row['NomeClassificacao'],
                contaativo = row['ContaAtivo'])
                list_aux.append(obj)
                
                if obj.realizado == 0:
                    self.futures.append(obj)
                
            return list_aux
            
        except Exception as e:
            print(e)

    def getContacts(self):
        try:
            url = '/api/pessoa/lista'
            endpoint = self.baseUrl + url
            
            list_contacts: list[Contact] = []
            for dict_ in super().get(endpoint=endpoint, headers=self.headers,type='json'): 
                emails_list = [email.strip() for email in dict_['Email'].split(',')] if dict_.get('Email') else None
                contact = Contact(
                    ID = dict_['ID'],
                    Nome = dict_['Nome'],
                    CPFCNPJ = dict_['CPFCNPJ'],
                    NomeFantasia = dict_['NomeFantasia'],
                    Logradouro = dict_['Logradouro'],
                    Nro = dict_['Nro'],
                    Complemento = dict_['Complemento'],
                    Bairro = dict_['Bairro'],
                    CEP = dict_['CEP'],
                    Cidade = dict_['Cidade'],
                    UF = dict_['UF'],
                    NomePais = dict_['NomePais'],
                    Ativo = dict_['Ativo'],
                    Email = dict_['EmailPrincipal'],
                    Telefone = dict_['TelefonePrincipal'],
                    Cliente = dict_['Cliente'],
                    Fornecedor = dict_['Fornecedor'],
                    Sexo = dict_['Sexo'],
                    RG = dict_['RG'],
                    OrgaoEmissorRG = dict_['OrgaoEmissorRG'],
                    UFEmissorRG = dict_['UFEmissorRG'],
                    ClienteDesde = dict_['ClienteDesde'],
                    IDClassificacaoPreferencial = dict_['IDClassificacaoPreferencial'],
                    IDCentroCustoPreferencial = dict_['IDCentroCustoPreferencial'],
                    Observacoes = dict_['Observacoes'],
                    ChavePix = dict_['ChavePix'],
                    TipoChavePix = dict_['TipoChavePix'],
                    EmailSecundario = emails_list[1] if (emails_list != None and len(emails_list) > 1) else None)
                list_contacts.append(contact)
            
            return list_contacts
        except Exception as e:
            status = 'Failed'
            logging.error(e)
        finally:
            status = 'Complete'
    
    # def getCategory(self, id:str=None, active:bool=False, onlyBank:bool=True) -> list[Category1]:
#     try
    #         url = '/api/financeiro/planoconta/lista'
    #         endpoint = self.baseUrl + url
        
    #         list_categories = list[Category1]
    #         for dict_category in super().get(endpoint=endpoint,headers=self.headers):
    #             dict_category = Category1(
    #                 id = dict_category['NumeroID'],
    #                 idplanoconta = dict_category['IDPlanoConta'],
    #                 idpai = dict_category['IDPai'],
    #                 nome = dict_category['Nome'],
    #                 ativo = dict_category['Ativo'],
    #                 controlasaldo = dict_category['ControlaSaldo'],
    #                 tipo = dict_category['Tipo'],
    #                 descricaotipo = dict_category['DescricaoTipo'],
    #                 cartaocredito = dict_category['CartaoCredito'],
    #                 tipocontagerencial = dict_category['TipoContaGerencial'],
    #                 idtipoimposto = dict_category['IDTipoImposto'],
    #                 nivel = dict_category['Nivel'],
    #                 grupocontacorrente = dict_category['GrupoContaCorrente'],
    #                 valoratual = dict_category['ValorAtual'],
    #                 saldobloqueado = dict_category['SaldoBloqueado'],
    #                 idcontabanco = dict_category['IDContaBanco'],
    #                 usarextratobanco = dict_category['UsarExtratoBanco'],
    #                 kamino = dict_category['Kamino'],
    #                 excluifluxocaixa = dict_category['ExcluiFluxoCaixa'],
    #                 codigoexterno = dict_category['CodigoExterno'],
    #                 dataultimoextratoconciliado = dict_category['DataUltimoExtratoConciliado'],
    #                 dataultimoextratopendente = dict_category['DataUltimoExtratoPendente'])
    #             list_categories.append(dict_category)
    #         status = 'Success'
    #         return list_categories
    #     except Exception as e:
    #         logging.error(f'{" "* 3} Erro: {e}')
    #         status = 'Failed'
    #     finally:
    #         print(f"Status: {status}")
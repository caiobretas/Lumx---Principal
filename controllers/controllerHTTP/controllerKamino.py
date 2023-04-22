import uuid
import datetime

from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase
from entities.entityTransfers import Transfer

from entities.entityTransaction import Transaction

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

    def postTransfer(self, obj: Transfer):
        url = '/api/financeiro/transferencia'
        endpoint = self.baseUrl + url

        super().post(endpoint=endpoint, obj=obj, headers=self.headers)

    def getTransfers(self, id: int = None, period_from: datetime.datetime =None, period_to: datetime.datetime=None) -> list[Transfer]:
        try:
            url = '/api/financeiro/transferencia/lista'
            
            filtros = f'?filtro.iD={id}&filtro.periodoDe={period_from}&filtro.periodoAte={period_to}'

            endpoint = self.baseUrl + url + filtros
            
            list_aux: list[dict] = []
            for dict_ in super().get(endpoint=endpoint, headers=self.headers):
                dict_ = Transfer(
                id = dict_['ID'],
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
            
            list_aux: list[Transaction] = [] 
            for row in super().get(type='csv', endpoint=endpoint, headers=self.headers):
                row: str = Transaction(
                id = row['ID'],
                tipo = row['Tipo'],
                data = datetime.datetime.strptime(row['Data'],'%d/%m/%Y').date(),
                datapagamento = datetime.datetime.strptime(row['DataPagamento'],'%d/%m/%Y').date() if row['DataPagamento'] != '' else None,
                datavencimento = datetime.datetime.strptime(row['DataVencimento'],'%d/%m/%Y').date(),
                datacompetencia = datetime.datetime.strptime(row['DataCompetencia'],'%d/%m/%Y').date(),
                valorprevisto = float(row['ValorPrevisto'].replace(',','.')),
                valorrealizado = float(row['ValorRealizado'].replace(',','.')) if row['ValorRealizado'] != '' else None,
                percentualrateio = float(row['PercentualRateio'].replace(',','.')) if row['PercentualRateio'] != '' else None,
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
                list_aux.append(row)
                
            return list_aux
            
        except Exception as e:
            print(e)
            
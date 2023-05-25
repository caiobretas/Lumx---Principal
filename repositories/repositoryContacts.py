import logging
from repositories.repositoryBase import RepositoryBase
from entities.entityContact import Contact

class RepositoryContacts(RepositoryBase):
    def __init__(self,connection, engine):
        self.schema = 'h_resources'
        self.tableName = 'contacts'
        super().__init__(connection, engine, self.schema, self.tableName)

    
    def insertContacts(self, list_contacts: list[Contact]) -> None:
        with self.cursor as cur:
            values = [t.to_tuple() for t in list_contacts]
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query =f"""
                    INSERT INTO
                        {self.schema}.{self.tableName}
                    (id, idpessoa, nome, cpfcnpj, nomefantasia, logradouro, nro,
                    complemento, bairro, cep, cidade, uf, nomepais, ativo, email,
                    telefone, cliente, fornecedor, sexo, rg, orgaoemissorrg, ufemissorrg,
                    clientedesde, idclassificacaopreferencial, idcentrocustopreferencial, 
                    observacoes, chavepix, tipochavepix, emailsecundario)
                    VALUES ({placeholders})
                    on conflict (idpessoa)
                    do update
                        set
                        nome = EXCLUDED.nome,
                        cpfcnpj = EXCLUDED.cpfcnpj,
                        nomefantasia = EXCLUDED.nomefantasia,
                        logradouro = EXCLUDED.logradouro,
                        nro = EXCLUDED.nro,
                        complemento = EXCLUDED.complemento,
                        bairro = EXCLUDED.bairro,
                        cep = EXCLUDED.cep,
                        cidade = EXCLUDED.cidade,
                        uf = EXCLUDED.uf,
                        nomepais = EXCLUDED.nomepais,
                        ativo = EXCLUDED.ativo,
                        email = EXCLUDED.email,
                        telefone = EXCLUDED.telefone,
                        cliente = EXCLUDED.cliente,
                        fornecedor = EXCLUDED.fornecedor,
                        sexo = EXCLUDED.sexo,
                        rg = EXCLUDED.rg,
                        orgaoemissorrg = EXCLUDED.orgaoemissorrg,
                        ufemissorrg = EXCLUDED.ufemissorrg,
                        clientedesde = EXCLUDED.clientedesde,
                        idclassificacaopreferencial = EXCLUDED.idclassificacaopreferencial,
                        idcentrocustopreferencial = EXCLUDED.idcentrocustopreferencial,
                        observacoes = EXCLUDED.observacoes,
                        chavepix = EXCLUDED.chavepix,
                        tipochavepix = EXCLUDED.tipochavepix,
                        emailsecundario = EXCLUDED.emailsecundario
                    """
                cur.executemany(query,values)
                self.connection.commit()
            except Exception as e:
                logging.error(e)
            # finally:
            #     status = 'Complete'
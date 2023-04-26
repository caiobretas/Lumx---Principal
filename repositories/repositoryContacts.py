from repositories.repositoryBase import RepositoryBase
from entities.entityContact import Contact


class RepositoryContacts(RepositoryBase):
    def __init__(self,connection, engine, schema, tableName):
        super().__init__(connection, engine, schema, tableName)

        
    def insertContacts(self, list_contacts: list[Contact]) -> None:
        with self.cursor as cur:
            values = [t.to_tuple() for t in list_contacts]
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query =f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id, idpessoa, nome, cpfcnpj, nomefantasia, logradouro, nro,
                    complemento, bairro, cep, cidade, uf, nomepais, ativo, email,
                    telefone, cliente, fornecedor, sexo, rg, orgaoemissorrg, ufemissorrg,
                    clientedesde, idclassificacaopreferencial, idcentrocustopreferencial, 
                    observacoes, chavepix, tipochavepix)
                    VALUES ({placeholders}) on conflict do nothing
                    """
                self.cursor.executemany(query,values)
                self.connection.commit()
            except:
                raise Exception
            # finally:
            #     status = 'Complete'
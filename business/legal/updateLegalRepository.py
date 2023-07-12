from entities.legal.entityDocument import LegalDocument
import logging
from repositories.legal.repositoryLegalDocuments import RepositoryLegalDocuments
from repositories.legal.repositoryDocuments import RepositoryDocuments

class UpdateLegalRepository:
    def __init__(self, connection, engine):
        self.connection = connection
        self.engine = engine
        
        self.repositoryDocuments = RepositoryDocuments(connection, engine)
        self.repositoryLegalDocuments = RepositoryLegalDocuments(connection, engine)
    
    def getDocumentsfromRepository(self):
    #  vamos definir o padrão para as minutas genéricas
        query = f'''
            select * from {self.repositoryDocuments.schema}.{self.repositoryDocuments.tableName}
            where drive = 'Jurídico'
        '''
        # lista de tuplas de documentos
        self.documents_list = self.repositoryDocuments.runQuery(query)
    
    def categorize(self, documents_list):
        # Categoriza os documentos com base no padrão: Caminho/Caminho/Nome/Nome/Nome
        documents_newlist = []
        for tuple_ in documents_list:
            document = LegalDocument(
                id = tuple_[0],
                googleid = tuple_[1],
                name = tuple_[2],
                type = tuple_[3],
                drive = tuple_[4],
                path = tuple_[5],
                weblink = tuple_[6],
                createdTime = tuple_[7],
                modifiedTime = tuple_[8],
                parents = tuple_[9])
            
            if document.trashed:
                document.categoria1 = 'Lixeira'
                continue
            
            list_ = []
            document.categoria1 = document.path.split('/')[0]
            document.categoria2 = (document.path.split('/')[1]).split('.')[0]
            
            list_.append(document.categoria1), list_.append(document.categoria2)
            list_ = list(tuple_)
            
            try:
                # Verifica se o nome possui categorias ou não.
                if len(document.path.split(' - ')) == 1:
                    document.name = document.path.split('/')[len(document.path.split('/'))-1]
                    documents_newlist.append(document)
                    continue
                
                document.categoria3 = (document.name.split(' - ')[0]).split('.')[0]
                try:
                    document.categoria4  = (document.name.split(' - ')[1]).split('.')[0]
                    document.categoria5  = (document.name.split(' - ')[2]).split('.')[0]
                    documents_newlist.append(document)
                except IndexError:
                    documents_newlist.append(document)
                    continue
            except:
                None
        return documents_newlist
            
    def update(self):
        self.getDocumentsfromRepository()
        categorizedDocuments: list[LegalDocument] = self.categorize(self.documents_list)
        self.repositoryLegalDocuments.insert(categorizedDocuments)
import os
from io import BytesIO
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.errors import HttpError
import logging
from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
from datetime import datetime
from googleapiclient.discovery import build, Resource

from entities.legal.entityDocument import Document
class GoogleDrive (ControllerGoogle):
    def __init__ (self):
        try:
            super().__init__()
            self.service: Resource = build('drive', 'v3', credentials=self.credential)
        except Exception as e:
            logging.error(e)
            
        self.files: list = []
            
    def getSharedDrives(self) -> list[dict]:
        'return a list of shared drives'
        return self.service.drives().list().execute()
    
    def deleteSharedDrives(self,driveId):    
        try:
           self.service.drives().delete(driveId=driveId).execute()
        except Exception as e:
            logging.error(e)
            
    def createFolder(self, name, parentId=None):
        """Create and return a folder.

        Param: parentId is used for sharedDrives as well.
        """ 
        folder_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parentId] if parentId else []
        }
        try:
            folder = self.service.files().create(body=folder_metadata,supportsAllDrives=True).execute()
            return folder
        except HttpError as err:
            logging.error(err)
    
    def uploadFile(self,file_bytes,file_name,folder_id):
        
        file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
        media = MediaIoBaseUpload(BytesIO(file_bytes), mimetype='application/octet-stream')
        
        try:
            return self.service.files().create(body=file_metadata, media_body=media, supportsAllDrives=True).execute()
        except HttpError as e:
            logging.error(e)
            return None

    def getFoldersList(self,driveId):

        # Lista para armazenar as pastas e subpastas
        pastas = []

        # Função recursiva para obter pastas e subpastas
        def obter_subpastas(pasta, prefixo):
            # Adicionar a pasta atual à lista
            pastas.append(prefixo + pasta['name'])

            # Fazer uma consulta para obter as subpastas da pasta atual
            consulta = f"'{pasta['id']}' in parents and mimeType = 'application/vnd.google-apps.folder'"
            resultados = self.service.files().list(q=consulta, corpora='drive', driveId=driveId, fields='files(id, name)',includeItemsFromAllDrives=True,supportsAllDrives=True).execute()
            subpastas = resultados.get('files', [])

            # Chamar recursivamente a função para cada subpasta encontrada
            for subpasta in subpastas:
                obter_subpastas(subpasta, prefixo + '--')

        # Fazer uma consulta para obter as pastas raiz do drive
        consulta = f"'{driveId}' in parents and mimeType = 'application/vnd.google-apps.folder'"
        resultados = self.service.files().list(q=consulta, corpora='drive', driveId=driveId, fields='files(id, name)',includeItemsFromAllDrives=True,supportsAllDrives=True).execute()
        pastas_raiz = resultados.get('files', [])

        # Chamar a função para cada pasta raiz encontrada
        for pasta_raiz in pastas_raiz:
            obter_subpastas(pasta_raiz, '')

        # Retornar a lista de pastas e subpastas
        return pastas
        
    def getFileParenting(self, fileId):
        """get file path and parenting"""
        try:
            # Obter metadados do arquivo
            file_metadata = self.service.files().get(fileId=fileId, fields='parents,name',supportsAllDrives=True).execute()

            # Obter o ID da pasta pai
            parent_id = file_metadata['parents'][0]

            # Obter metadados da pasta pai
            parent_metadata = self.service.files().get(fileId=parent_id, fields='name, parents',supportsAllDrives=True).execute()

            # Criar uma lista para armazenar os objetos de pasta
            folder_objects = [{'name': parent_metadata['name'], 'id': parent_id}]

            # Criar uma lista para armazenar os nomes das pastas pai
            path = [parent_metadata['name']]

            # Iterar até encontrar a pasta raiz
            while 'parents' in parent_metadata:
                parent_id = parent_metadata['parents'][0]
                parent_metadata = self.service.files().get(fileId=parent_id, fields='name, parents',supportsAllDrives=True).execute()
                folder_objects.append({'name': parent_metadata['name'], 'id': parent_id})
                path.append(parent_metadata['name'])

            # Inverter a lista para obter o caminho completo
            path.reverse()
            folder_objects.reverse()

            # Adicionar o prefixo ao caminho completo
            path_with_prefix = "Drives compartilhados/" + '/'.join(path)

            # Adicionar o nome do arquivo ao caminho completo
            path_with_filename = path_with_prefix + '/' + file_metadata['name']

            # Imprimir o caminho completo com o nome do arquivo
            print(path_with_filename)

            # Imprimir os objetos de pasta
            for folder_obj in folder_objects:
                print(f"Nome do parent: {folder_obj['name']}, Parent ID: {folder_obj['id']}")

        except Exception as e:
            print(f"Erro: {e}")

    def getFilesByDriveId(self, driveId, parent_path='', driveName=None,):
        
        try:
            """Listar todos os arquivos em um diretório e subdiretórios."""
            results = self.service.files().list(
                q="'{}' in parents".format(driveId),
                fields="files(name, mimeType, id, webViewLink, createdTime, modifiedTime, parents, trashed)",
                pageSize=1000,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True
            ).execute()
            files = results.get('files', [])
            
            for file in files:
                file_name = file['name']
                document = Document(
                    googleid=file.get('id'),
                    name=file_name,
                    type=file.get('mimeType').split('.')[-1],
                    drive = driveName,
                    path=os.path.join(parent_path, file_name),
                    weblink=file.get('webViewLink'),
                    createdTime=datetime.strptime(file.get('createdTime'), "%Y-%m-%dT%H:%M:%S.%fZ"),
                    modifiedTime=datetime.strptime(file.get('modifiedTime'), "%Y-%m-%dT%H:%M:%S.%fZ"),
                    parents=file.get('parents')[0],
                    trashed = file.get('trashed')
                )
                if document.type != 'folder': self.files.append(document) 

                if document.type == 'folder':
                    self.getFilesByDriveId(document.googleid, document.path, driveName)
                    # self.getFilesByDriveId(document.googleid)
                    
        except HttpError as he:
            logging.error(he)
        
        return self.files
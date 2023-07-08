import datetime

from uuid import uuid4, UUID
class Document:
    def __init__(self, id=None, googleid=None, name=None, type=None, drive=None, path=None, weblink=None,createdTime=None, modifiedTime=None, parents=None):
        self.id = str(uuid4()) if not id else id
        self.googleid: str = googleid
        self.name: str = name.split('.')[0]
        self.type: str = type
        self.drive: str = drive
        self.path: str = path
        self.webLink: str = weblink
        self.createdTime: datetime.datetime =createdTime
        self.modifiedTime: datetime.datetime = modifiedTime
        self.parents: str = parents
    
    def __repr__(self):
        return f'{self.name}'
    
    def to_tuple(self) -> tuple:
        return (self.id,self.googleid,self.name,self.type,self.drive,self.path,self.webLink,self.createdTime,self.modifiedTime,self.parents)

class LegalDocument(Document):
    def __init__(self, id=None, googleid=None, name=None, type=None, drive=None, path=None, weblink=None,createdTime=None, modifiedTime=None, parents=None,categoria1=None,categoria2=None,categoria3=None,categoria4=None,categoria5=None,idparte=None,dataassinatura=None):
        super().__init__(id,googleid, name, type, drive, path, weblink,createdTime, modifiedTime, parents)    
        
        self.categoria1 = categoria1
        self.categoria2 = categoria2
        self.categoria3 = categoria3
        self.categoria4 = categoria4
        self.categoria5 = categoria5
        self.idparte = idparte
        self.dataassinatura = dataassinatura
        
        
    def __repr__(self):
        return f'{self.name}'
    
    def to_tuple(self) -> tuple:
        return (self.id,self.name,self.categoria1,self.categoria2,self.categoria3,self.categoria4,self.categoria5)

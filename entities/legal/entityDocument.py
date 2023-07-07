import datetime

from uuid import uuid4, UUID
class Document:
    def __init__(self, id=None, googleid=None, name=None, type=None, drive=None, path=None, weblink=None,createdTime=None, modifiedTime=None, parents=None):
        self.id = str(uuid4()) if not id else id
        self.googleid = googleid
        self.name = name
        self.type = type
        self.drive = drive
        self.path = path
        self.webLink = weblink
        self.createdTime =createdTime
        self.modifiedTime = modifiedTime
        self.parents = parents
    
    def __repr__(self):
        return f'{self.name}'
    
    def to_tuple(self) -> tuple:
        return (self.id,self.googleid,self.name,self.type,self.drive,self.path,self.webLink,self.createdTime,self.modifiedTime,self.parents)

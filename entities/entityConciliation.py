import math
class Conciliation:
    def __init__(self, hash: str, methodid:str, description: str = None, project: str = None):
        self.hash = hash if hash else None
        self.methodid = methodid if methodid else None
        self.description = description if description else None
        self.project = project if project else None
    def __repr__(self) -> str:
        return f'Method ID: {self.methodid} - Project: {self.project} - Description: {self.description}'
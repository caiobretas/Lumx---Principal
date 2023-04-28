class Conciliation:
    def __init__(self, hash: str, methodid:str, description: str = None, project: str = None):
        self.hash = hash
        self.methodid = methodid
        self.description = description
        self.project = project
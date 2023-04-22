class ContaOrigem:
    def __init__(self, id, name, hierarchy = None, type=None):
        self.id = id
        self.name = name
        self.hierarchy = hierarchy
        self.type = type

    def __str__(self):
        return f'\n     ID_Conta: {self.id}\n     Nome_Conta: {self.name}\n'
    
    def __repr__(self):
        return f'\n     ID_Conta: {self.id}\n     Nome_Conta: {self.name}\n'
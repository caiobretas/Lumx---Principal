class Blockchain:
    def __init__(self, id, name, symbol, secret_type):
        
        self.id = id
        self.name = name
        self.symbol = symbol
        self.secret_type = secret_type
        
    def __str__(self):
        return f'ID: {self.id} - Name: {self.name.capitalize()} - Symbol: {self.symbol}'
    
    def __repr__(self):
        return f'ID: {self.id} - Name: {self.name.capitalize()} - Symbol: {self.symbol}'
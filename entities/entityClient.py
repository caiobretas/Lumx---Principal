class Client:
    
    def __init__(self, id, name, key, is_active):
        self.id = id
        self.name = name
        self.key = key
        self.is_active = is_active

    def __str__(self):
        return f'ID: {self.id} - Name: {self.name.capitalize()}'
    
    def __repr__(self):
        return f'ID: {self.id} - Name: {self.name.capitalize()}'

class User:

    def __init__(self, id, client_id, username, created_at, avatar_url, email, cpf, phone, mynt_address):

        self.id = id
        self.client_id = client_id
        self.username = username
        self.created_at = created_at
        self.avatar_url = avatar_url
        self.email = email
        self.cpf = cpf
        self.phone = phone
        self.mynt_address = mynt_address
    
    def __str__(self) -> str:
        return f'\n\nID: {self.id}\nUsername: {self.username}\nAddress: {self.mynt_address}\n'
    
    def __repr__(self) -> str:
        return f'\n\nID: {self.id}\nUsername: {self.username}\nAddress: {self.mynt_address}\n'
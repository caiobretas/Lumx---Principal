class Wallet:
    def __init__(self, id, user_id, address, external_id, provider, pin_code, created_at, updated_at, is_archived) -> None:
    
        self.id = id
        self.user_id = user_id
        self.address = address
        self.external_id = external_id
        self.provider = provider
        self.pin_code = pin_code
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_archived = is_archived

    def __str__(self):
        return f'ID: {self.id} - Address: {self.address}'
    def __repr__(self):
        return f'ID: {self.id} - Address: {self.address}'
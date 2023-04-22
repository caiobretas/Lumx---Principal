class Collection:

    def __init__(self, id, client_id, name, description, banner_url, contract_id, image_url, crossmint_id, currency, random_description, random_image_url, random_item_name, send_matic):
        self.id = id
        self.client_id = client_id
        self.name = name
        self.description = description
        self.banner_url = banner_url
        self.contract_id = contract_id
        self.image_url = image_url
        self.crossmint_id = crossmint_id
        self.currency = currency
        self.random_description = random_description
        self.random_image_url = random_image_url
        self.random_item_name = random_item_name
        self.send_matic = send_matic

    def __str__(self):
        return f'ID: {self.id} - Name: {self.name.capitalize()}'
    
    def __repr__(self):
        return f'ID: {self.id} - Name: {self.name.capitalize()}'
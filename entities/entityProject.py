class Project:
    def __init__(self, collection_id, collection_name, client_id, client_name, client_royalties, client_royalties_address, contract_address, blockchain_symbol):
        self.id = collection_id
        self.collection_name = collection_name
        self.client_id = client_id
        self.client_name = client_name
        self.client_royalties = client_royalties
        self.client_royalties_address = client_royalties_address
        self.contract_address = contract_address
        self.blockchain_symbol = blockchain_symbol
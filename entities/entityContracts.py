class Contracts:
    def __init__(self, id, client_id, blockchain_id, name, description, contract_address, base_uri, max_address, created_at, general_sale_starts_at, general_sale_ends_at, presale_starts_at, presale_ends_at, royalties, royalties_address, supply):

        self.id = id
        self.client_id = client_id
        self.blockchain_id = blockchain_id
        self.name = name
        self.description = description
        self.contract_address = contract_address
        self.base_uri = base_uri
        self.max_address = max_address
        self.created_at = created_at
        self.general_sale_starts_at = general_sale_starts_at
        self.general_sale_ends_at = general_sale_ends_at
        self.presale_starts_at = presale_starts_at
        self.presale_ends_at = presale_ends_at
        self.royalties = royalties
        self.royalties_address = royalties_address
        self.supply = supply
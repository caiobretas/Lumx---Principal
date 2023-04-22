class MintRequest:
    def __init__(self, id, price, created_at, item_id, txhash, amount, collection_id, wallet_id, status_id):
        self.id = id
        self.price = price
        self.created_at = created_at
        self.item_id = item_id
        self.txhash = txhash
        self.amount = amount
        self.collection_id = collection_id
        self.wallet_id = wallet_id
        self.status_id = status_id
    
    def __str__(self) -> str:
        return f'\n\nWallet ID: {self.wallet_id}\nCollection ID: {self.collection_id}\nItem ID: {self.item_id}\nData: {self.created_at}\nPrice: {self.price}\nAmount: {self.amount}\nStatus: {self.status_id}\n\n'
    
    def __repr__(self) -> str:
        return f'\n\nWallet ID: {self.wallet_id}\nCollection ID: {self.collection_id}\nItem ID: {self.item_id}\nData: {self.created_at}\nPrice: {self.price}\nAmount: {self.amount}\nStatus: {self.status_id}\n\n'
    
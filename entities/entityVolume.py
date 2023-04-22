from datetime import datetime
import pytz

class Volume:
    def __init__(self, id, txhash, datetime, collection_id, type,price, amount, currency, blockchain, status_id):
        
        self.id = id
        self.txhash = txhash
        self.collection_id = collection_id
        self.client_id = None
        self.status_id = status_id
        self.datetime = datetime
        self.type = type
        self.price = price
        self.amount = amount
        self.volume = None
        self.currency = currency
        self.blockchain = blockchain
        self.volumeBRL = None
        self.coinPrice = 0
        

class VolumeWallets:

    def __init__(self, id, client_id, updated_at, address, provider, is_archived):
        
        self.id = id
        self.client_id = client_id
        self.datetime = updated_at
        self.address = address
        self.provider: str = provider
        self.is_archived = is_archived

    def __str__(self):
        return f'Provedor: {self.provider.capitalize()} - Data: {self.datetime} - Address: {self.address} - Arquivada: {self.is_archived}'
    
    def __repr__(self):
        return f'Provedor: {self.provider.capitalize()} - Data: {self.datetime} - Address: {self.address} - Arquivada: {self.is_archived}'
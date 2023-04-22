class Controle:
    def __init__(self, date: str, client_id: str, client_name: str):
        self.date = date
        self.client_id = client_id
        self.client_name = client_name
        
        self.wallets_onCustody = None
        self.fiat_volumePrimary = None
        self.crypto_volumePrimary = None
        self.coin_Primary = None
        self.coinPrice_volumePrimary = None
        self.volumePrimary_BRL = None
        self.crypto_volumeSecondary = None
        self.coin_Secondary = None
        self.coinPrice_volumeSecondary = None
        self.volumeSecondary_BRL = None
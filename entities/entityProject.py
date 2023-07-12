class Project:
    def __init__(self, id = None, project_name = None, client_id = None, client_royalties_address = None, contract_address = None, blockchain_symbol = None, ativo = None, statusupdatedate = None, currency = None, currencycrypto = None, setupfee = None, maintancefee = None, primarysalefee = None, secondarysalefee = None, pixfee = None, min_pixfee = None, creditcardfee = None, connect = None, activeuser = None, wallet = None):
        
        self.id = id
        self.project_name = project_name
        self.client_id = client_id
        self.client_royalties_address = client_royalties_address
        self.contract_address = contract_address
        self.blockchain_symbol = blockchain_symbol
        self.ativo = ativo
        self.statusupdatedate = statusupdatedate
        self.currency = currency
        self.currencycrypto = currencycrypto
        self.setupfee = setupfee
        self.maintancefee = maintancefee
        self.primarysalefee = primarysalefee
        self.secondarysalefee = secondarysalefee
        self.pixfee = pixfee
        self.min_pixfee = min_pixfee
        self.creditcardfee = creditcardfee
        self.connect = connect
        self.activeuser = activeuser
        self.wallet = wallet

    def to_tuple(self):
        return (self.id,self.project_name,self.client_id,self.client_royalties_address,self.contract_address,self.blockchain_symbol,self.ativo,self.currency,self.currencycrypto,self.setupfee,self.maintancefee,self.primarysalefee,self.secondarysalefee,self.pixfee,self.min_pixfee,self.creditcardfee,self.connect,self.activeuser,self.wallet)
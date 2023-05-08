class Book:
    def __init__(self, address = None, name = None, is_lumx: bool = None, is_safe: bool = False, blockchain: str = None,  is_conversion: bool = None, is_primarysale: bool = None, is_secondarysale: bool = None, project: str = None):

        self.address = str(address).strip().lower()
        self.name = name
        self.is_lumx = is_lumx
        self.is_safe = is_safe
        self.blockchain = blockchain if blockchain != 'False' else None
        self.is_conversion = is_conversion
        self.is_primarysale = is_primarysale
        self.is_secondarysale = is_secondarysale
        self.project = project if project != 'False' else None
    
    def __repr__(self) -> str:
        return f'Address: {self.address} - Name: {self.name}'
    def __str__(self) -> str:
        return f'Address: {self.address} - Name: {self.name}'
    
    def to_tuple(self) -> tuple:
        return (self.address, self.name, self.is_lumx, self.is_safe, self.blockchain, self.is_conversion, self.is_primarysale, self.is_secondarysale, self.project)
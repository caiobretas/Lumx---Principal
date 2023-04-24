class Book:
    def __init__(self, address = None, name = None, is_lumx: bool = False, is_conversion: bool = False, is_primarysale: bool = False, is_secondarysale: bool = False):

        self.address = address
        self.name = name
        self.is_lumx = is_lumx
        self.is_conversion = is_conversion
        self.is_primarysale = is_primarysale
        self.is_secondarysale = is_secondarysale
    
    def __repr__(self) -> str:
        return f'Address: {self.address} - Name: {self.name}'
    def __str__(self) -> str:
        return f'Address: {self.address} - Name: {self.name}'
    
    def to_tuple(self) -> tuple:
        return (self.address, self.name, self.is_lumx, self.is_conversion, self.is_primarysale, self.is_secondarysale)
    
class Book:
    def __init__(self, address = None, name = None, is_lumx: bool = False, is_conversion: bool = False, is_primarysale: bool = False, is_secondarysale: bool = False):

        self.address = address
        self.name = name
        self.is_lumx = is_lumx
        self.is_conversion = is_conversion
        self.is_primarysale = is_primarysale
        self.is_secondarysale = is_secondarysale
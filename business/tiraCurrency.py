from entities.entityVolume import Volume

class TiraCurrency:
    def __init__(self, lst: list[Volume]):
        for obj in lst:
            if obj.currency == 'fiat' and obj.type == 'secondary':
                obj.currency = 'crypto'
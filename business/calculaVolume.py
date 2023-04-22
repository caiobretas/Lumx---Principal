from entities.entityVolume import Volume

class CalculaVolume:
    
    def calculaVolume(lst: list[Volume]):
        for obj in lst:
            obj.volume = obj.price * obj.amount

    def calculaVolumeBRL(lst: list[Volume]):
        for obj in lst:
            if obj.type == 'primary' and obj.currency != 'fiat':
                obj.volumeBRL = obj.coinPrice * obj.volume
            elif obj.type == 'primary' and obj.currency == 'fiat':
                obj.volumeBRL = obj.volume
            elif obj.type == 'secondary':
                obj.volumeBRL = obj.coinPrice * obj.volume
import datetime

class Coin:
    def __init__(self,  high, low, open, volumefrom, volumeto, close, conversiontype, conversionsymbol, date=None, id=None, time=None):
        self.id = str(time) + str(conversionsymbol) if id is None else id
        self.time = float(time) if time is not None else None
        date = datetime.datetime.fromtimestamp(self.time) + datetime.timedelta(hours=3) if date == None else date
        self.date: datetime.datetime = date.date()
        if high != None: self.high = float(high)
        else: self.high = 0
        self.low = float(low)
        self.open = float(open)
        self.volumefrom = float(volumefrom)
        self.volumeto = float(volumeto)
        self.close = float(close)
        self.conversiontype = str(conversiontype)
        self.conversionsymbol = str(conversionsymbol)

    def to_tuple(self) -> tuple:
        return (self.id, self.time, self.date, self.high, self.low, self.open, self.volumefrom, self.volumeto, self.close, self.conversiontype, self.conversionsymbol)

    def __repr__(self) -> str:
        return f'ID: {self.id} - Date: {self.date} - Symbol: {self.conversionsymbol}'
    def __str__(self) -> str:
        return f'Coin'
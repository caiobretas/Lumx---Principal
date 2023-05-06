from entities.entityCoin import Coin

from viewers.viewerBase import ViewerBase
import pandas as pd

class ViewerPrices( ViewerBase ):

    def __init__(self, path: str, sheetName: str):

        self.path = path
        self.sheetName = sheetName

    def abreDataFrame(self) -> pd.DataFrame:
        return pd.read_excel(
            io = self.path,
            sheet_name=self.sheetName,
            header=0
        )
        
    def insertPrices(self, list_obj: list[Coin]=None, list_dict=None):
        if list_obj != None:
            super().salvaExcel(list_=list_obj)
        if list_dict != None:
            super().salvaExcel(dict_=list_dict)
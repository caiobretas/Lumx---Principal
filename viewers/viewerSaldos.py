from entities.entityBalance import Balance
import pandas as pd
from viewers.viewerBase import ViewerBase

class ViewerSaldos ( ViewerBase ):
    def __init__ (self, path: str, sheetName: str):
       self.path = path
       self.sheetName = sheetName
    
    def abreDataFrame(self) -> pd.DataFrame:
        return pd.read_excel(
            io = self.path,
            sheet_name=self.sheetName,
            header=0
        )
    
    def insertViewerPrices(self, lst: list[Balance]):
        super().salvaExcel(lst)
from entities.entityControle import Controle

from viewers.viewerBase import ViewerBase

import pandas as pd

class ViewerControle( ViewerBase ):

    def __init__(self, path: str, sheetName: str = 'Controle'):
        super().__init__(path=path, sheetName=sheetName)
        self.path = path
        self.sheetName = sheetName

    def abreDataFrame(self) -> pd.DataFrame:
        return pd.read_excel(
            io = self.path,
            sheet_name=self.sheetName,
            header=0
        )
    
    def insertViewerControle(self, lst: list[Controle]):
        super().salvaExcel(lst)

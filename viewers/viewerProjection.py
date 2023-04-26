from entities.entityProjection import Projection

from viewers.viewerBase import ViewerBase
import pandas as pd

class ViewerProjection( ViewerBase ):

    def __init__(self, path: str, sheetName: str):

        self.path = path
        self.sheetName = sheetName

    def abreDataFrame(self) -> pd.DataFrame:
        return pd.read_excel(
            io = self.path,
            sheet_name=self.sheetName,
            header=0
        )
    
    def insertViewerProjection(self, lst: list[Projection]):
        super().salvaExcel(lst)

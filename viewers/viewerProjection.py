from entities.entityProjection import Projection

from viewers.viewerBase import ViewerBase
import pandas as pd

class ViewerProjection( ViewerBase ):

    def __init__(self, path: str, sheetName: str):

        self.path = path
        self.sheetName = sheetName

    def abreDataFrame(self) -> pd.DataFrame:
        super().abreDataFrame()
    
    def insertViewerProjection(self, lst: list[Projection]):
        super().salvaExcel(lst)

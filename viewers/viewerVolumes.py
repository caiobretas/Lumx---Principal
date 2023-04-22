from entities.entityVolume import Volume, VolumeWallets 

from viewers.viewerBase import ViewerBase

import pandas as pd

class ViewerVolumes( ViewerBase ):

    def __init__(self, path: str, sheetName: str):

        self.path = path
        self.sheetName = sheetName

    def abreDataFrame(self) -> pd.DataFrame:
        return pd.read_excel(
            io = self.path,
            sheet_name=self.sheetName,
            header=0
        )
    
    def insertViewerVolumes(self, lst: list[Volume]):
        super().salvaExcel(lst)

    def insertViewerVolumeWallets(self, lst: list[VolumeWallets]):
        super().salvaExcel(lst)

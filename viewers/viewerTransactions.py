from viewers.viewerBase import ViewerBase
from entities.entityTransaction import Transaction

class ViewerTransactions ( ViewerBase ):

    def __init__(self, path, sheetName):
        super().__init__(path, sheetName)
    
    def insertViewerMovements(self, lst: list[Transaction]):
        super().salvaExcel(lst)
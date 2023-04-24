import pandas as pd
from pandas import DataFrame

class InterfaceBase:
    def __init__(self, path: str, sheetName: str):
        
        self.path = path
        self.sheetName = sheetName
    
    def abreDataFrame(self) -> pd.DataFrame:
        try:
            return pd.read_excel(
            io=self.path,
            sheet_name=self.sheetName,
            header=0
        )
        except:
            raise Exception
    
    def salvaInterface(self, lst: list):
        with pd.ExcelWriter(path=self.path, mode='a', if_sheet_exists='overlay') as writer:
            try:
                dataFrame: DataFrame = pd.DataFrame([vars(obj) for obj in lst])
                
                dataFrame.to_excel(
                    writer, 
                    sheet_name=self.sheetName, 
                    index=False,
                    engine='openpyxl',
                    # float_format="%.2f",
                )
            except Exception as ex:
                print("Houve um erro ao salvar dados na Interface. \n{}".format(ex))

    
    # def inserePedido(self, dataFrame: pd.DataFrame):
    #     with pd.ExcelWriter(path=self.path, mode='a', if_sheet_exists='new') as writer:


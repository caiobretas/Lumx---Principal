from pandas import DataFrame
import pandas as pd

class ViewerBase:

    def __init__(self, path: str, sheetName: str):
        
        self.path = path
        self.sheetName = sheetName

    def abreDataFrame(self) -> pd.DataFrame:
        return pd.read_excel(
            io=self.path,
            sheet_name=self.sheetName,
            header=0
        )   
    def salvaExcel(self, lst: list):
        with pd.ExcelWriter(path=self.path, mode='a', if_sheet_exists='overlay') as writer:
            try:
                dataFrame: DataFrame = pd.DataFrame([vars(obj) for obj in lst])
                if 'datetime' in dataFrame.columns:
                    dataFrame['datetime'] = pd.to_datetime(dataFrame['datetime']).dt.tz_localize(None)
                
                dataFrame.to_excel(
                    writer, 
                    sheet_name=self.sheetName, 
                    index=False,
                    engine='openpyxl',
                    # float_format="%.5f",
                )
            except Exception as ex:
                print("Houve um erro ao salvar dados no excel. \n{}".format(ex))
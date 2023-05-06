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
            engine='openpyxl',
            header=0
        )   
    def salvaExcel(self,list_:list=None,dict_:dict=None):
        with pd.ExcelWriter(engine='openpyxl',path=self.path, mode='a', if_sheet_exists='replace') as writer:
            try:
                if list_ != None:
                    dataFrame: DataFrame = pd.DataFrame([vars(obj) for obj in list_])
                    if 'datetime' in dataFrame.columns:
                        dataFrame['datetime'] = pd.to_datetime(dataFrame['datetime']).dt.tz_localize(None)
                        
                if dict_ != None:
                    dataFrame = pd.DataFrame(dict_)
                
                dataFrame.to_excel(
                    writer, 
                    sheet_name=self.sheetName, 
                    index=False,
                    engine='openpyxl'
                    # float_format="%.5f"
                    )
    
            except Exception as ex:
                print("Houve um erro ao salvar dados no excel. \n{}".format(ex))
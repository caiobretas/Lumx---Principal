from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
import logging
import gspread   

class GoogleSheets(ControllerGoogle):
    def __init__(self):
        super().__init__()
        try:
            self.client = gspread.authorize(credentials=self.credential)
        except Exception as e:
            logging.error(e)
            
    def getRow(self, rowNumber, sheetName, worksheetId: str):
        try:
            worksheet: gspread.Spreadsheet = self.client.open_by_key(worksheetId)
            sheet: gspread.Worksheet = worksheet.worksheet(sheetName)
            return sheet.row_values(rowNumber)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
            
    def appendRow(self, values: list, sheetName, worksheetId: str):
        try:
            worksheet: gspread.Spreadsheet = self.client.open_by_key(worksheetId)
            sheet: gspread.worksheet.Worksheet = worksheet.worksheet(sheetName)
            sheet.append_row(values)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
    
    def clearSheet(self,worksheetId,sheetName=None,headers=False):
        worksheet = self.client.open_by_key(worksheetId)
        sheet = worksheet.worksheet(sheetName)
        headers = self.getRow(1,sheetName,worksheetId) if headers is None else headers
        sheet.clear()
            
    def overwriteWorksheet_byID(self,worksheetId:str,list_values:list,sheetName=None,range=None,headers=None):
        if list_values != None:
            try:
                worksheet = self.client.open_by_key(worksheetId)
                
                sheet = worksheet.worksheet(sheetName)
                
                headers = self.getRow(1,sheetName,worksheetId) if headers is None else headers
                sheet.clear()
                sheet.append_row(values=headers, table_range='A1')
                sheet.append_rows(values=list_values,table_range=range)
                
            except Exception as e:
                logging.error(f'{" "* 3} Erro: {e}')
        else:
            None
            
    
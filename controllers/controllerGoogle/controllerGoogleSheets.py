from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
from googleapiclient.errors import HttpError
import logging
import gspread

class GoogleSheets(ControllerGoogle):
    def __init__(self):
        super().__init__()
        try:
            self.client = gspread.authorize(credentials=self.credential)
            self.worksheetId = None
            self.sheetId = None
        
        except Exception as e:
            logging.error(e)
    
    def openSheet(self, worksheetId:not None,SheetId=None) -> gspread.Worksheet | gspread.Spreadsheet:
        try:
            if SheetId:
                worksheet: gspread.Spreadsheet = self.client.open_by_key(worksheetId)
                sheet: gspread.models.Worksheet = worksheet.get_worksheet_by_id(SheetId)
                
                self.worksheetId = worksheetId
                self.sheetId = SheetId
                
                return sheet
            else:
                worksheet: gspread.Spreadsheet = self.client.open_by_key(worksheetId)
                return worksheet
            
        except HttpError as err:
            logging.error(err)
        except Exception as e:
            logging.error(e)
    
    def writemanyRows(self, listofRow: not None):
        if not listofRow: return
        sheet = self.openSheet(self.worksheetId, self.sheetId)
        sheet.append_rows(listofRow)
    
    def writeRow(self, values: list,worksheetId:not None,SheetId=None, table_range=None) -> None:
        sheet = self.openSheet(worksheetId,SheetId)
        if table_range:
            sheet.append_row(values, table_range=table_range)
            return
        sheet.append_row(values)
        
    def eraseSheet(self,worksheetId=None,SheetId=None, headers=None):
        if self.worksheetId: worksheetId = self.worksheetId
        if self.sheetId: SheetId = self.sheetId
        if headers:
            sheet = self.openSheet(worksheetId,SheetId)
            sheet.clear()
            self.writeRow(headers, worksheetId, SheetId)
        else:
            sheet = self.openSheet(worksheetId,SheetId) 
            sheet.clear()
        
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
            sheet: gspread.models.Worksheet = worksheet.worksheet(sheetName)
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
            
    
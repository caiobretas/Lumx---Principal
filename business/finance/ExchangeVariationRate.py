from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from repositories.repositoryPrices import RepositoryPrices
from repositories.repositoryTransactions import RepositoryTransactions

class ExchangeVariationRate:
    def __init__(self,connection,engine):
        self.repositoryPrices = RepositoryPrices(connection,engine)
        self.repositoryTransactions = RepositoryTransactions(connection,engine)
        self.controllerGoogleSheets = GoogleSheets()
        self.worksheetId = '1CDumW0Wpy4OlYWsh8R_zOKSGFyfK2oFnXMeoY24qbGk'
        
    def getExchangeRate(self):
        pricesVariaton: list = self.repositoryPrices.getExchangeVariation()
        return pricesVariaton
    
    def writeTransactions(self):

        sheetId = 391759750
        headers = ['id','data','moeda','valorrealizado','valorrealizado_brl','subcategoria4']
        
        transactions = self.repositoryTransactions.getTransactions()
        
        
        # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
        filteredTransactions = []
        for transaction in transactions:
            aux_list = []
            if transaction[6]:
                aux_list.append(transaction[0])
                aux_list.append(transaction[7].strftime('%Y-%m-%d'))
                aux_list.append(transaction[13])
                aux_list.append(transaction[10])
                aux_list.append(transaction[12])
                aux_list.append(transaction[16])
                filteredTransactions.append(aux_list)
        
        filteredTransactions.sort(reverse=True)
        
        # open sheet 
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        # erase old values
        self.controllerGoogleSheets.eraseSheet(headers=headers)
        # write new values
        self.controllerGoogleSheets.writemanyRows(filteredTransactions)
        return None
            
    
    def writePrices(self):
        sheetId = 56497729
        headers = ['id', 'data', 'token']
        
        prices: list = self.repositoryPrices.getPrices()
        
        # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
        filteredPrices = []
        for price in prices:
            aux_list = []
            if price.close and price.conversionsymbol != 'BRL':
                aux_list.append(price.id)
                aux_list.append(price.date.strftime('%Y-%m-%d'))
                aux_list.append(price.close)
                filteredPrices.append(aux_list)
        
        filteredPrices.sort(reverse=True)
        
        # open sheet 
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        # erase old values
        self.controllerGoogleSheets.eraseSheet(headers=headers)
        # write new values
        self.controllerGoogleSheets.writemanyRows(filteredPrices)
        return None

    def writeExchangeRate(self):
        sheetId = 573968761
        headers = ['id', 'data', 'token', 'variação']
        
        # write prices daily variation in Google Sheets
        pricesVariatons = self.getExchangeRate()
        
        # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
        filteredPricesVariations = []
        for priceVariation in pricesVariatons:
            aux_list = []
            if priceVariation[3] and priceVariation[2] != 'BRL':
                aux_list.append(priceVariation[0])
                aux_list.append(priceVariation[1].strftime('%Y-%m-%d'))
                aux_list.append(priceVariation[2])
                aux_list.append(priceVariation[3])
                filteredPricesVariations.append(aux_list)
        
        filteredPricesVariations.sort(reverse=True)
        
        # open sheet 
        self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
        # erase old values
        self.controllerGoogleSheets.eraseSheet(headers=headers)
        # write new values
        self.controllerGoogleSheets.writemanyRows(filteredPricesVariations)
        
    def updateSheet(self):
        self.writeTransactions()
        self.writePrices()
        self.writeExchangeRate()
        
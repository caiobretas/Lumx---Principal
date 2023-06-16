import logging
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from repositories.repositoryPrices import RepositoryPrices
from repositories.repositoryTransactions import RepositoryTransactions
from entities.entityTransaction import Transaction

class ExchangeVariationRate:
    def __init__(self,connection,engine):
        self.repositoryPrices = RepositoryPrices(connection,engine)
        self.repositoryTransactions = RepositoryTransactions(connection,engine)
        self.controllerGoogleSheets = GoogleSheets()
        self.worksheetId = '1CDumW0Wpy4OlYWsh8R_zOKSGFyfK2oFnXMeoY24qbGk'
    
    def getBalance(self):
        self.repositoryTransactions.ge
     
    def getExchangeRate(self):
        pricesVariaton: list = self.repositoryPrices.getExchangeVariation()
        return pricesVariaton
    
    def writeTransactions(self):
        
        try:

            sheetId = 391759750
            headers = ['id','data','moeda','valorrealizado','valorrealizado_brl','subcategoria4']
            
            transactions: list[Transaction] = self.repositoryTransactions.getTransactions()
            
            # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
            filteredTransactions = []
            for transaction in transactions:
                aux_list = []
                obj: Transaction  = transaction[0]
                
                if obj.realizado:
                    
                    aux_list.append(obj.id)
                    aux_list.append(obj.datapagamento.strftime('%Y-%m-%d'))
                    aux_list.append(obj.moeda)
                    aux_list.append(obj.valorrealizado)
                    aux_list.append(obj.valorrealizado_brl)
                    aux_list.append(transaction[1])
                    
                    filteredTransactions.append(aux_list)
            
            filteredTransactions.sort(reverse=True)
            
            # open sheet
            self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
            # erase old values
            self.controllerGoogleSheets.eraseSheet(headers=headers)
            # write new values
            self.controllerGoogleSheets.writemanyRows(filteredTransactions)
            return None
        
        except Exception as e:
            logging.error(e)
            return None    
    
    def writePrices(self):
        sheetId = 56497729
        headers = ['id', 'date', 'token', 'price']
        
        prices: list = self.repositoryPrices.getProjection()
        
        # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
        filteredPrices = []
        for price in prices:
            aux_list = []
            if price.close and price.token != 'BRL':
                aux_list.append(price.id)
                aux_list.append(price.date.strftime('%Y-%m-%d'))
                aux_list.append(price.token)
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
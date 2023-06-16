from time import time
import datetime
import logging
import pygsheets
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from repositories.repositoryPrices import RepositoryPrices
from repositories.repositoryTransactions import RepositoryTransactions
from entities.entityTransaction import Transaction

class ExchangeVariationRate:
    def __init__(self,connection,engine):
        print()
        self.repositoryPrices = RepositoryPrices(connection,engine)
        self.repositoryTransactions = RepositoryTransactions(connection,engine)
        self.controllerGoogleSheets = GoogleSheets()
        self.worksheetId = '1CDumW0Wpy4OlYWsh8R_zOKSGFyfK2oFnXMeoY24qbGk'
    
    def getBalance(self) -> list:
        # get the current balance from our wallets
        return self.repositoryTransactions.getBalance()
        
    def getExchangeRate(self) -> list:
        pricesVariaton: list = self.repositoryPrices.getExchangeVariation()
        return pricesVariaton
    
    def getFinantialRevenue(self):
        
        balance_list = self.getBalance()
        exchangeRate_list = self.getExchangeRate()
        
    def writeBalance(self):
        print('\nWriting balance...')
        try:
            start_time = time()
            sheetId = 1397884468
            headers = ['id','moeda','data','saldolocal','saldobrl']
            balance_list = self.getBalance()
            
            # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
            filteredList = []
            for balance in balance_list:
                aux_list = []
                date: datetime.datetime = balance[1]
                formatted_date = (date.date() - datetime.date(1899, 12, 30)).days
                id = f'{formatted_date}{balance[0]}'
                aux_list.append(id)
                aux_list.append(balance[0])
                aux_list.append(formatted_date)
                aux_list.append(balance[2])
                aux_list.append(balance[3])
                    
                filteredList.append(aux_list)
            
            self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
            # erase old values
            self.controllerGoogleSheets.eraseSheet(headers=headers)
            # write new values
            self.controllerGoogleSheets.writemanyRows(filteredList)
            status = 'Success'
        except Exception as e:
            logging.error(e)
            status = 'Failed'
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
    
    def writeTransactions(self):
        print('\nWriting transactions...')
        try:
            start_time = time()
            sheetId = 391759750
            headers = ['id','data','moeda','valorrealizado','valorrealizado_brl','subcategoria4']
            
            transactions: list[Transaction] = self.repositoryTransactions.getTransactions()
            
            # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
            filteredTransactions = []
            for transaction in transactions:
                aux_list = []
                obj: Transaction  = transaction[0]
                
                if obj.realizado:
                    date = obj.datapagamento
                    formatted_date = (date.date() - datetime.date(1899, 12, 30)).days
                    aux_list.append(obj.id)
                    aux_list.append(formatted_date)
                    aux_list.append(obj.moeda)
                    aux_list.append(obj.valorrealizado)
                    aux_list.append(obj.valorrealizado_brl)
                    aux_list.append(transaction[1])
                    
                    filteredTransactions.append(aux_list)
            
            # open sheet
            self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
            # erase old values
            self.controllerGoogleSheets.eraseSheet(headers=headers)
            # write new values
            self.controllerGoogleSheets.writemanyRows(filteredTransactions)
            
            status = 'Success'
            return None
        
        except Exception as e:
            logging.error(e)
            status = 'Failed'
            
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
    
    def writePrices(self):
        print('\nWriting prices...')
        sheetId = 56497729
        headers = ['id', 'date', 'token', 'price']
        
        prices: list = self.repositoryPrices.getProjection()
        
        # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
        filteredPrices = []
        try:
            start_time = time()
            for price in prices:
                aux_list = []
                if price.close and price.token != 'BRL':
                    date = price.date
                    formatted_date = (date - datetime.date(1899, 12, 30)).days
                    id = f'{formatted_date}{price.token}'
                    aux_list.append(id)
                    aux_list.append(formatted_date)
                    aux_list.append(price.token)
                    aux_list.append(price.close)
                    filteredPrices.append(aux_list)
            
            # open sheet
            self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
            # erase old values
            self.controllerGoogleSheets.eraseSheet(headers=headers)
            # write new values
            self.controllerGoogleSheets.writemanyRows(filteredPrices)
            status = 'Sucess'
            return None
        except Exception as e:
            logging.error(e)
            status = 'Failed'
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))

    def writeExchangeRate(self):
        sheetId = 573968761
        headers = ['id', 'data', 'token', 'variação']
        print('\nWriting exchange rate variations...')
        # write prices daily variation in Google Sheets
        pricesVariatons = self.getExchangeRate()
        
        # filters the rows that are going to be written (by default, all rows with no ExchangeRate are ignored)
        filteredPricesVariations = []
        try:
            start_time = time()
            for priceVariation in pricesVariatons:
                aux_list = []
                if priceVariation[2] != 'BRL':
                    date: datetime = priceVariation[1]
                    formatted_date = (date - datetime.date(1899, 12, 30)).days
                    id = f"{formatted_date}{priceVariation[2]}"
                    aux_list.append(id)
                    aux_list.append(formatted_date)
                    aux_list.append(priceVariation[2])
                    aux_list.append(priceVariation[3])
                    filteredPricesVariations.append(aux_list)
            
            # open sheet 
            self.controllerGoogleSheets.openSheet(self.worksheetId,sheetId)
            # erase old values
            self.controllerGoogleSheets.eraseSheet(headers=headers)
            # write new values
            self.controllerGoogleSheets.writemanyRows(filteredPricesVariations)
            status = 'Sucess'
        except Exception as e:
            logging.error(e)
            status = 'Failed'
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
                 
    def updateSheet(self):
        self.writeBalance()
        self.writeTransactions()
        self.writePrices()
        self.writeExchangeRate()
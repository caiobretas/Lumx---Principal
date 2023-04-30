from entities.entityTransaction import TransactionCrypto
import logging
class TreatCryptoTransactions:

    def categories(self, obj: TransactionCrypto, list_wallets, list_conversion, list_primarysale, list_secondarysale):
        if (obj.from_ in list_conversion) or (obj.to_ in list_conversion):
            obj.methodId = '0x2130'
            obj.description = 'Conversão monetária'
        if obj.from_ in list_primarysale:
            obj.methodId = '0x48s5'
            obj.description = 'Venda primária'
        if obj.from_ in list_secondarysale:
            obj.methodId = '0x5sap1'
            obj.description = 'Venda secundária'
        if (obj.from_.lower() in list_wallets) and (obj.to_.lower() in list_wallets):
            obj.methodId = '0x110'
            obj.description = 'Transferência entre contas'
            
    def __init__(self, obj: TransactionCrypto, list_wallets: list, list_conversion: list, list_primarysale: list, list_secondarysale: list):
        
        try:
            self.categories(
                obj, list_wallets, list_conversion, list_primarysale, list_secondarysale)
       
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
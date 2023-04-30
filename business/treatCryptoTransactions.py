from entities.entityTransaction import TransactionCrypto

class TreatCryptoTransactions:
    
    def gasFee_rules(self, obj: TransactionCrypto):
        # if obj.txnType.lower() == 'internal'
        obj.gasPrice = 0 if obj.gasPrice == None else obj.gasPrice
        if str(obj.txnType).strip().lower() != 'erc-20':
            obj.gasFee = 0 if obj.address != obj.from_ else (-1) * ((obj.gasUsed * obj.gasPrice)  if obj.gasUsed != None else 0)
        else:
            obj.gasFee = 0 if obj.address != obj.from_ else (-1) * ((obj.gasUsed * obj.gasPrice) if obj.gasUsed != None else 0)
        obj.gasFee = 0 if str(obj.txnType).strip().lower() == 'Internal' else (0  if obj.gasFee == None else obj.gasFee)
    
    def totalValue(self, obj: TransactionCrypto):
        obj.total = obj.value + obj.gasFee

    def categories(self, obj: TransactionCrypto, list_wallets, list_conversion, list_primarysale, list_secondarysale):
        if obj.from_ or obj.to_ in list_conversion:
            obj.methodId = '0x2130y'
            obj.description = 'Conversão monetária'
        if obj.from_ or obj.to_ in list_primarysale:
            obj.methodId = '0x48s5'
            obj.description = 'Venda primária'
        if obj.from_ or obj.to_ in list_secondarysale:
            obj.methodId = '0x5sap1'
            obj.description = 'Venda secundária'
        if obj.from_ and obj.to_ in list_wallets:
            obj.methodId = '0x110'
            obj.description = 'Transferência entre contas'
            
    def __init__(self, transactionCrypto: TransactionCrypto, list_wallets: list, list_conversion: list, list_primarysale: list, list_secondarysale: list):
        self.gasFee_rules(transactionCrypto)
        self.totalValue(transactionCrypto)
        self.categories(self, transactionCrypto, list_wallets, list_conversion, list_primarysale, list_secondarysale)
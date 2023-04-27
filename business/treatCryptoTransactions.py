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

    def __init__(self, transactionCrypto: TransactionCrypto):
        self.gasFee_rules(transactionCrypto)
        self.totalValue(transactionCrypto)

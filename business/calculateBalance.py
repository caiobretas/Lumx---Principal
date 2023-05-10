from entities.entityProjection import Projection
from entities.entityBankAccount import BankAccount
from business.assembleProjection import AssembleProjection

class CalculateBalance:
    def __init__(self, obj: Projection):
        bankAccount = BankAccount(obj.contaativo)
        bankAccount.deposit(obj.valorrealizado)
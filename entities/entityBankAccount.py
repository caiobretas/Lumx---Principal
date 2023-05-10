from datetime import datetime
class BankAccount:
    def __init__(self, name: str):
        self.name = name
        self.current_balance = 0.0
    
    def deposit(self, amount: float, coin: str):
        self.current_balance += amount
        
    
    # def withdraw(self, amount: float):
    #     if amount > self.current_balance:
    #         raise ValueError("Saldo insuficiente!")
    #     self.current_balance -= amount

class Account:
    def __init__ (self,balance,accountno):
        self.balance = balance
        self.accountno = accountno
    
    def debit (self,amount):
        self.balance -=amount
        print(amount,"is debited")
    
    def credit (self,amount):
        self.balance -=amount
        print(amount,"is credited")

    def print(self):
        print("Toal Balance : ",self.balance,"Account no : ",self.accountno)

a1 = Account(1000,12)

a1.debit(1100)
# a1.credit()
a1.print()

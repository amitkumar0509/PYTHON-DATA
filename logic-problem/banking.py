class bank:
    def __init__(self,name,acc_no,balance=0):
        self.name = name
        self.acc_no = acc_no
        
        self.balance = balance
    def deposit(self,amount):  
        if amount >0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.acc_no}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.acc_no}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
bank1 =bank("AMIT",700562901,7676)
NEW = bank1.deposit(100009090)
print(bank1.balance)
NEW = bank1.deposit(100009090)
print(bank1.balance)
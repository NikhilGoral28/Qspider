class BankAccount:
    def __init__(self,cname,balance):
        self.cname = cname
        self.balance = balance

    def deposit(self,amt):
        if amt < 0:
            raise  ValueError("Amount should be greater than 0")
        self.balance += amt
        print(f"{amt} is Deposited")
        print(f"Updated balance is {self.balance}")

    def withdraw(self,amt):
        if amt > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amt
        print(f"{amt} is Debited")
        print(f"Updated balance is {self.balance}")
    
    def display(self):
        print(f"Customer Name: {self.cname}")
        print(f"Balance: {self.balance}")

class SavingAccount(BankAccount):

    def __init__(self, cname, balance):
        super().__init__(cname, balance)

    def withdraw(self, amt):
        if amt < 10000:
            raise ValueError("Amount should be more than 10000 to withdraw")
        self.balance -= amt
        print(f"{amt} is Debited")
        print(f"Updated balance is {self.balance}")

class SalaryAccount(BankAccount):
    def __init__(self, cname, balance,acctno):
        super().__init__(cname, balance)
        self.acctno = acctno

    def deposit(self, amt):
        if amt < 20000:
            raise ValueError("Deposite amount should be more than 20000")
        self.balance += amt
        print(f"{amt} is Deposited")
        print(f"Updated balance is {self.balance}")

    def display(self):
        super().display()
        print(f"Account Number: {self.acctno}")


s1 = SavingAccount('smith',89000)
s2 = SalaryAccount("allen",98000,1234)

try:
    s1.display()
    s1.deposit(1000)
    s1.withdraw(30000)
except Exception as e:
    print(f"Error : {e}")


print()
try:
    s2.display()
    s2.deposit(40000)
    s2.withdraw(5000)
except Exception as e:
    print(f"Error : {e}")
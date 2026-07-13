class Balance:
    def checkBalance(self):
        print(f"Initial Balance is : {self.balance}/-\n")

class deposite:
    def deposite_amt(self,amt):
        if amt >0:
            self.balance += amt
            print(f"{amt}/- : has been deposited")
            print(f"Updated balance : {self.balance}/-\n")
        
        else:
            print("Invalid Amount\n")
        

class withdraw:
    def withdraw_amt(self,amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"{amt}/-: has been debited")
            print(f"Updated Balance : {self.balance}/-\n")
        
        else:
            print("Insuffisient Balance\n")
    
class Bank(Balance,deposite,withdraw):
    
    def __init__(self,cname,actno,balance):
        self.cname = cname
        self.actno = actno
        self.balance = balance 
    
    def display(self):
        print(f"Custome Name: {self.cname}")
        print(f"Account Number: {self.actno}")
        print(f"Opening Balance: {self.balance}/-\n")



c1 = Bank("smith",124,90000)
c1.display()
c1.checkBalance()
c1.deposite_amt(1200)
c1.withdraw_amt(800)

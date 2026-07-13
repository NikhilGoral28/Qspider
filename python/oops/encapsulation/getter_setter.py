class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,new):
        if isinstance(new,int):
            self.__balance = new
        
        else:
            raise ValueError("Invalid format")


obj = BankAccount(89999)
try:
    obj.balance = '450000'
    print(obj.balance)
except Exception as e:
    print(e)

print(obj.balance)

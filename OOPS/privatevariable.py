class BankAccount:
    customer_name:str
    mpin:int
    acc_type:str
    balance:int
    def __init__(self,customer_name,mpin,acc_type,balance):
        self.customer_name=customer_name
        self.__mpin=mpin
        self.acc_type=acc_type
        self.__balance=balance
    def get_balance(self):
        print(self.__balance)
    
    def __str__(self):
        return self.customer_name

BankAccount_inst=BankAccount("Hari",1234,"savings",10000)
print(BankAccount_inst)
BankAccount_inst.get_balance()

class Bank:
    acno:int
    balance:int
    ac_type:str
    customer_name:str
    
    def __init__(self,acno,balance,ac_type,customer_name):
            self.acno=acno
            self.balance=balance
            self.ac_type=ac_type
            self.customer_name=customer_name


    def deposit(self,amount):
        self.balance+=amount
        print(f"Your account {self.acno} has been credited with amount of {amount} avl bal is {self.balance}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        
        else:
            self.balance-=amount
            print(f"Your account {self.acno} has been debited with amount of {amount} avl bal is {self.balance}")
    
    def get_balance(self):
        print(f"avl bal is {self.balance}")

bank_inst=Bank(1200890112,12000,"savings","Navya")
bank_inst.withdraw(12000)
bank_inst.deposit(10000)
bank_inst.get_balance()


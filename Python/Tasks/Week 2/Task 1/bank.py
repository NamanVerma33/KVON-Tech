# Create a Bank Account Class:
# Attributes: Name, Balance, Account Number
# Methods:
# deposit(amount) → Add money to balance
# withdraw(amount) → Deduct money if balance > amount
# show_balance() → Show current balance

class Bank:
    def __init__(self,name,accNo,balance):
        self.name = name
        self.balance = balance
        self.accNo = accNo
    
    def show_balance(self):
        print(f"Bank Balance Details:\nName: {self.name}\nAccount number: {self.accNo}\nBalance: {self.balance}Rs")

    def deposit(self,amount):
        self.balance += amount
        self.show_balance()
    
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance -= amount
            self.show_balance()
        else:
            print("Sorry! Your bank balance has not sufficient amount")
  
print("Welcome to the XYZ Bank:")
name = input("Enter your Name: ").strip()
accNo = int(input("Enter the account number"))
balance = int(input("Enter your amount: "))

customer = Bank(name,accNo,balance)

while True:
    option = int(input("Enter the operation you want to perform: \n1)Deposit Amount\n2)Withdraw Amount\n3)Show Balance \n4)Exit"))
    if option==1:
        amount =int(input("Enter the amount you want to deposit"))
        customer.deposit(amount)
    elif option==2:
        amount =int(input("Enter the amount you want to widthdraw"))
        customer.withdraw(amount)
    elif option==3:
        customer.show_balance()
    elif option==4:
        break




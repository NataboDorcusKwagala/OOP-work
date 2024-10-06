class BankAccount:
    #interest rate shared by all accounts
    interest_rate = 0.05
    
    def __init__(self,account_holder):
        #account holder's name
        self.account_holder = account_holder
        #the initial balance is set to 0
        self.balance = 0
        
    def deposit(self, amount):
        #add deposited ammount to the balance
        self.balance += amount
        
    def withdraw(self,amount):
        #if the funds are suffient subtract the amount
        if amount <= self.balance:
            self.balance-= amount
        
        #print error if the balance is not enough    
        else:
            print("insuffient funds")
            
            
    def apply_interest(self):
        #add interet to the balance
        self.balance += self.balance * BankAccount.interest_rate
        
        
    def display_account_info(self):
        #Show the account holder and their balance
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")
        
#making 3 accounts      
Account001 = BankAccount("Namusubuga Shine")
Account007 = BankAccount("Tomolo John")
Account050 = BankAccount("John Harny")

#operations for Account001
Account001.deposit(100000000)
Account001.withdraw(1000000)
Account001.apply_interest()
Account001.display_account_info()


#operations for Account007
Account007.deposit(1000000)
Account007.withdraw(500000)
Account007.apply_interest()
Account007.display_account_info()


#operations for Account050
Account050.deposit(2000000000)
Account050.withdraw(2000000)
Account050.apply_interest()
Account050.display_account_info()



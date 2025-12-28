# Bank Operation Using OOP
from datetime import datetime
class Bank:
    bankname = 'kumari Bank Limited'
    branch = 'kathmandu,Nepal'

    # create account
    def __init__(self, username, address, pan):
        self.username = username
        self.address = address
        self.pan = pan
        self.balance = 0.0
        self.transactions = []
        print(f'Hello {self.username}\n congratulation! Your Account Created Successfully')
    # deposit
    def deposit(self, amount):
        if amount>0:
            self.balance=self.balance+amount
            self.transactions.append((datetime.now(), "Deposit", amount, self.balance))
            print(f"Rs.{amount} deposited successfully")
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            self.transactions.append((datetime.now(), "Withdraw", amount, self.balance))
            print(f"Rs.{amount} withdraw successfully")
        else:
            print(f" INSUFFICENT AMOUNT IN ACCOUNT\n Rs.{amount} withdraw failed")

    def bank_statement(self):
        print("\n========== BANK STATEMENT =====================")
        print(f"Account Holder : {self.username}")
        print(f"Account Address : {self.address}")
        print(f"Account Pan : {self.pan}")
        print("---------------------------------------------------")
        print("Date & Time           Type      Amount     Balance")
        print("----------------------------------------------------")
        for t in self.transactions:
            print(f"{t[0].strftime('%Y-%m-%d')}   {t[1]:<8}  Rs.{t[2]:<8} Rs.{t[3]}")
        print("-----------------------------------------------------")
        print(f"Available Balance : Rs.{self.balance}")
        print("=====================================================\n")

print(f'Welcome to {Bank.bankname}' , f'{Bank.branch}')
username = input('Enter your Name:')
pan = int(input('Enter your PAN card number: '))
address = input("Enter your Address: ")

b = Bank(username, address, pan)

while True:
    print("Please Select Any Option")
    print(" 1. Deposit\n 2. Withdraw\n 3. Mini Statement\n 4. Exit")
    option=int(input('Enter your Option: '))
    if option==1:
       amount= float(input('Enter Deposit Amount(NPR):-'))
       b.deposit(amount)
    if option==2:
        amount= float(input('Enter Withdraw Amount(NPR):-'))
        b.withdraw(amount)

    if option==3:
        b.bank_statement()

    if option==4:
        print(f'Thank your for using {b.bankname}')
        break
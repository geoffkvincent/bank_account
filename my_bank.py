import time
account = 0

class MyBank:
    def __init__(self):
        print('')
        print('--------$$$ Welcome to MyBank $$$-----------')
        print('------------------------------------------')
        print("It looks like you don't have an account with us.")
        print("Would you like to open one today?  (y/n) ")
        user_input = input()
        if user_input == 'y':
            self.getAmountFromConsole()
        elif user_input == 'n':
            time.sleep(2)
            exit()
        else:
            print('Invalid Input')
            time.sleep(2)
            MyBank()

    def getAmountFromConsole(self): 
        global account  
        user_input = eval(input('Enter Amount: $'))
        account = user_input
        print('Your current balance is: $%d ' % account)
        time.sleep(2)

    def menu(self):
        print('------------------------')
        print('Please make a selection:')
        print('------------------------')
        print('1) Make a Deposit ')
        print('2) Make a Withdrawl')
        print('3) Current Balance')
        print('4) Exit')
        user_input = eval(input())
        self.menu_switch(user_input)
        
    def menu_switch(self, user_input):
        if user_input == 1:
            self.deposit()
        elif user_input == 2:
            self.withdraw()
        elif user_input == 3:
            self.balance()
        elif user_input == 4:
            exit()
        else:
            print('Invalid Input')
            time.sleep(2)
            self.menu()

    def deposit(self):
        global account
        user_input = eval(input('Enter Deposit Amount: $'))
        account += user_input
        print("Your money's been successfully deposited")
        time.sleep(1)
        self.menu()

    def withdraw(self):
        global account
        user_input = eval(input('How much would you like to withdraw?: $'))
        account -= user_input
        time.sleep(1)
        self.menu()

    def balance(self):
        global account
        print('============================')
        print('Your current balance is: $%d' % account)
        time.sleep(1)
        self.menu()

bank = MyBank()
bank.menu()
# bank.getAmountFromConsole()
# print(account)
# bank.deposit()
# print(account)
# bank.withdraw()
# print(account)
# bank.balance()


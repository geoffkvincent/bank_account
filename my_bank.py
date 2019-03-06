account = 0

class MyBank:
    def __init__(self):
        print('Welcome to My Bank')
        print('------------------')
        print("It looks like you don't have an account with us.")
        print("Would you like to open one today?  (y/n) ")
        user_input = input()
        if user_input == 'y':
            self.getAmountFromConsole()
        elif user_input == 'n':
            sleep(2)
            exit()
        else:
            print('Invalid Input')
            sleep(2)
            MyBank()

    def getAmountFromConsole(self): 
        global account  
        user_input = eval(input('Enter Amount: $'))
        account = user_input
        print('Your current balance is: $%d ' % account)

    def deposit(self):
        global account
        user_input = eval(input('Enter Deposit Amount: $'))
        account += user_input

    def withdraw(self):
        global account
        user_input = eval(input('How much would you like to withdraw?: $'))
        account -= user_input

    def balance(self):
        global account
        print('Your current balance is %d' % account)

bank = MyBank()
bank.getAmountFromConsole()
print(account)
bank.deposit()
print(account)
bank.withdraw()
print(account)
bank.balance()


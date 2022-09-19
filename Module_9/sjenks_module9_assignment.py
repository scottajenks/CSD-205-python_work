# Scott Jenks - 9/18/2022 - Module 9 Assignment

# Program using classes to represent a bank account


class BankAccount:
    """A simple attempt to model a bank account"""

    def __init__(self, accountNumber, balance):
        """Initialize account number and balance attributes"""
        self.account_number = accountNumber
        self.account_balance = float(balance)

    def withdrawl(self):
        """Withdraw funds from account"""
        withdraw_amount = input("\nHow much would you like to withdrawl? ")

        # Make sure input is a numerical value
        try:
            withdraw_amount = float(withdraw_amount)
        except ValueError:
            print("\tPlease only enter a numerical value.\n")
            withdraw_amount = input("\nHow much would you like to withdrawl? ")
            withdraw_amount = float(withdraw_amount)

        # Calculate new account balance
        new_account_balance = self.account_balance - withdraw_amount

        # Check to see if withdrawl takes account negative
        while new_account_balance < 0:
            print(
                f"\nYou cannot withdraw ${withdraw_amount:.2f} from account '{self.account_number}' as you only have ${self.account_balance:.2f} and it will take your account negative.")
            """Withdraw funds from account"""
            withdraw_amount = input("\nHow much would you like to withdraw? ")

            # Make sure input is a numerical value
            try:
                withdraw_amount = float(withdraw_amount)
            except ValueError:
                print("\tPlease only enter a numerical value.\n")
                withdraw_amount = input(
                    "\nHow much would you like to withdrawl? ")
                withdraw_amount = float(withdraw_amount)

            # Calculate new account balance
            new_account_balance = self.account_balance - withdraw_amount

        else:
            print(
                f"\nYou are withdrawing ${withdraw_amount:.2f} from account '{self.account_number}' so your new balance in the account is ${new_account_balance:.2f}.")
            print("\n\tThank you for banking with Python Bank.")
            input("\n\t\tPress Enter to exit.")

    def deposit(self):
        """Deposits funds into account"""
        deposit_amount = input("\nHow much would you like to deposit? ")

        # Make sure input is a numerical value
        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            print("\tPlease only enter a numerical value.\n")
            deposit_amount = input("\nHow much would you like to deposit? ")
            deposit_amount = float(deposit_amount)

        # Calculate new account balance
        new_account_balance = self.account_balance + deposit_amount
        self.account_balance = new_account_balance

        print(
            f"\nYou are depositing ${deposit_amount:.2f} into account '{self.account_number}' so your new balance in the account is ${self.account_balance:.2f}.")
        print("\n\tThank you for banking with Python Bank.")
        input("\n\t\tPress Enter to exit.")

    def getBalance(self):
        """Returns balance of account"""
        print(f"\nYou current balance is ${self.account_balance:.2f}.")

        # Ask if customer wants to deposit or withdraw money
        deposit_withdraw = input(
            "\nWould you like to deposit or withdraw money? 'Y' - 'N': ")
        deposit_withdraw = deposit_withdraw.title()

        # Ask weather they are depositing or withdrawing
        if deposit_withdraw == 'Y':
            answer = input("\nDeposit or Withdrawl? 'D' - 'W': ")
            answer = answer.title()
            if answer == 'D':
                self.deposit()
            else:
                self.withdrawl()
        else:
            print("\n\tThank you for banking with Python Bank.")
            input("\n\t\tPress Enter to exit.")


class CheckingAccount(BankAccount):
    """Represents aspects of a checking account"""

    def __init__(self, accountNumber, balance):
        """Initialize attributes of the parent class.
        Then initialize attributes specifice to a checking account"""
        super().__init__(accountNumber, balance)
        self.fee = float(5)
        self.minimum_balance = float(50)

    def deductFees(self):
        """Add fee if account balance is below minimum balance"""
        if self.account_balance < self.minimum_balance:
            fee_balance = self.account_balance - self.fee
            print(f"Your checking account '{self.account_number}' has a balance of ${self.account_balance:.2f}. Due to being under the minimum balance of ${self.minimum_balance:.2f} there was a fee of ${self.fee:.2f} charged to the account so your new balance is ${fee_balance:.2f}.")

    def checkMinimumBalance(self):
        """Checks to make sure balance isn't below the account minimum"""
        if self.account_balance > self.minimum_balance:
            min_balance_diff = self.account_balance - self.minimum_balance
            print(f"Your checking account '{self.account_number}' has a balance of ${self.account_balance:.2f}. You have ${min_balance_diff:.2f} to withdraw before you reach the minimum balance of ${self.minimum_balance:.2f} and get charged a fee of ${self.fee:.2f}.")


class SavingsAccount(BankAccount):
    """Represents aspects of a savings account"""

    def __init__(self, accountNumber, balance):
        """Initialize attributes of the parent class.
        Then initialize attributes specifice to a checking account"""
        super().__init__(accountNumber, balance)
        self.interestRate = float(0.02)

    def addInterest(self):
        """Calulate interest and add to balance"""
        interest = self.interestRate * self.account_balance
        new_balance = interest + self.account_balance
        print(f"Your savings account '{self.account_number}' has a balance of ${self.account_balance:.2f}. With the 2% interest you will receive ${interest:.2f} so your new balance will be ${new_balance:.2f}.")


my_savings_account = SavingsAccount(123456, 200)
my_savings_account.addInterest()
print()

my_savings_account = SavingsAccount(123456, 25)
my_savings_account.addInterest()
print()


my_checking_account = CheckingAccount(123456, 200)
my_checking_account.deductFees()
print()
my_checking_account.checkMinimumBalance()
print()

my_checking_account = CheckingAccount(123456, 25)
my_checking_account.deductFees()
print()
my_checking_account.checkMinimumBalance()
print()

input("\n\t\tPress Enter to exit.")


'''my_bank_account = BankAccount(123456, 200)

welcome = input(
    "Welcome to Python Bank. \nWould you like to make a deposit, withdrawl or check balance? 'D' - 'W' - 'B': ")
welcome = welcome.title()

if welcome == 'D':
    my_bank_account.deposit()
elif welcome == 'W':
    my_bank_account.withdrawl()
elif welcome == 'B':
    my_bank_account.getBalance()
else:
    print("\n\tThank you for banking with Python Bank.")'''

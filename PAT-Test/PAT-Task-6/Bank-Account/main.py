# -----------------------------
# Base Class
# -----------------------------

class BankAccount:

    def __init__(self, account_number, balance, interest_rate):  # create savings account
        self.account_number = account_number                     # store account number
        self._balance = balance                                  # protected balance with encapsulation 
        self.interest_rate = interest_rate                       # store interest rate

    def deposit(self, amount):                                   # deposit money
        print("Account Number:", self.account_number)
        print("Opening Balance Rs.", self._balance)              # show opening balance
        self._balance += amount                                  # add money to balance
        print("Deposited Rs.", amount)
        print("Balance Rs.", self._balance)

    def withdraw(self, amount):                                  # withdraw money 
        if amount <= self._balance:                              # check if enough money
            self._balance -= amount                              # subtract money
            print("Withdrawn Rs.", amount)
            print("Balance Rs.", self._balance)
        else:
            print("Not enough balance")

# -----------------------------
# Savings Account
# -----------------------------

class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, interest_rate):  # create savings account
        super().__init__(account_number, balance, interest_rate) # call parent constructor
        self.interest_rate = interest_rate                       # store interest rate
        print("Interest rate %",interest_rate)

    def calculate_interest(self):                                # calculate interest
        interest = self._balance * self.interest_rate / 100
        print("Interest gained Rs.", interest)

# -----------------------------
# Current Account
# -----------------------------

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance): # create current account
        super().__init__(account_number, balance, 0)              # call parent constructor with 0 interest
        self.minimum_balance = minimum_balance                    # store minimum balance

    def withdraw(self, amount):                                   # override withdraw method to maintain minimum balance
        if self._balance - amount >= self.minimum_balance:
            self._balance -= amount
            print("Withdrawn Rs.", amount)
            print("Balance Rs.", self._balance)
        else:
            print("Minimum balance Rs.", self.minimum_balance, "/- must be maintained")


# -----------------------------
# Main Program
# -----------------------------

s1 = SavingsAccount("GUVI_Savings_Ac_100", 1000, 5)                         # create savings account with account number, balance and interest rate
s1.deposit(200)
s1.withdraw(300)
s1.calculate_interest()


print("\n")

c1 = CurrentAccount("GUVI_Current_Ac_100", 2000, 500)                          # create current account with account number, balance and minimum balance
c1.deposit(500)
c1.withdraw(1800)
c1.withdraw(1000)

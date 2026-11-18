

# ## Bank Account Details
# -------------------------------------------------------
# Create a class BankAccount whose constructor accepts:
#
#  account number
#  account holder name
#  balance
#
# Add a method to display all the account details neatly.
# -----------------------------------------------------------

class Bank:

    def __init__(self,acc_no,holder,balance):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def details(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Holder Name: {self.holder}")
        print(f"Balance: {self.balance}")

b1 = Bank(1235097, "Anusree", 89000)
b1.details()

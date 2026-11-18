

# create a class  BankAccount with instance varibles
# accno , holdername , balance
# add a static varible bank name
# create 2 account objects and print their details
# =========================================================
class BankAccount:
    bank_name = "SBI"

    def acc(self,acc_no,hol_name,balance):
        self.acc_no = acc_no
        self.hol_name = hol_name
        self.balance = balance

    def acc_details(self):
        print("Account No:",self.acc_no)
        print("Holder Name:",self.hol_name)
        print("Available Balance:",self.balance)
        print("Bank Name:",BankAccount.bank_name)

ac1 = BankAccount()
ac1.acc(103494681,"Anu",56000)
ac1.acc_details()
print("="*25)
ac2 = BankAccount()
ac2.acc(10657687,"Abhi",65000)
ac2.acc_details()

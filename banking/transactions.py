
from django.contrib.auth.models import User
from banking.models import Account


class BankAccount(object):
    def __init__(self):
        pass
    def withdraw():
        pass
    def deposit():
        pass

class CurrentAccount(BankAccount):

    def __init__(self):
        self.balance = 0

    def get_account(user):
        return Account.objects.get(acc_owner=user)

    def deposit(self, amount, user):
        account = self.get_account(user)
        account.acc_balance += amount
        account.save()


    def withdraw(self, amount, user):
        account = self.get_account(user)
        if account.acc_balance < amount:
            raise ValueError("Cannot withdraw beyond the current account balance")
        account.acc_balance -= amount
        account.save()

    def transfer(self, user, amount, recipient, accNumber):
        rec = User.objects.get(username=recipient)
        rec_account = Account.objects.get(acc_number=accNumber)
        if rec and rec_account:
            self.withdraw(self, amount, user)
            self.deposit(self, amount, rec)


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

    def get_account(request):
        return Account.objects.get(acc_owner=request.user)

    def deposit(self, amount, request):
        account = self.get_account(request)
        account.acc_balance += amount
        account.save()


    def withdraw(self, amount, request):
        account = self.get_account(request)
        if account.acc_balance < amount:
            raise ValueError("Cannot withdraw beyond the current account balance")
        account.acc_balance -= amount
        account.save()

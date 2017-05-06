
# banking/views.py - Views for the banking app
from banking.forms import *
from banking.models import *
from banking.transactions import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
import string
import random


#@csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'reg_form': form
    })

    return render_to_response(
    'registration.html',
    variables,
    )

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                variables = RequestContext(request, {'user': user })
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    variables = RequestContext(request, {
    'login_form': form
    })
    return render_to_response( 'login.html', variables )

def about_page(request):
    return render_to_response( 'about.html' )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

#@login_required(login_url="login/")
def home_page(request):
    reg_form = RegistrationForm()
    login_form = LoginForm()
    variables = RequestContext(request, {
        'login_form': login_form,
        'reg_form': reg_form,
        'user': request.user
        })
    return render_to_response('index.html', variables)

@login_required(login_url="/login/")
def account_create_page(request):
    if request.method == 'POST':

        if Account.objects.filter(acc_owner=request.user).count() > 0:
            messages.add_message(request, messages.INFO, 'You can only create one account')
            messages.warning(request, 'You already have an account.')
            return HttpResponseRedirect('/account/')

        acc_form = AccountCreateForm(request.POST)
        if acc_form.is_valid():
            account = Account(
            acc_name=acc_form.cleaned_data['acc_name'],
            acc_balance=acc_form.cleaned_data['acc_balance'],
            acc_owner=request.user,
            acc_number=''.join(random.choice(string.digits) for _ in range(12))
            )
            account.save()
            return HttpResponseRedirect('/account/')
    else:
        acc_form = AccountCreateForm()
    variables = RequestContext(request, {
        'acc_form': acc_form,
        'user': request.user })
    return render_to_response('account_create.html', variables)


def get_account(request):
    return Account.objects.get(acc_owner=request.user)


@login_required(login_url="/login/")
def account_page(request):
    if Account.objects.filter(acc_owner=request.user).count() <= 0:
        messages.add_message(request, messages.INFO, 'Please create an account first')
        messages.warning(request, 'Please create an account first')
        return HttpResponseRedirect('/account/create/')
    else:
        account = get_account(request)
        variables = RequestContext(request, {
            'user': request.user,
            'account': account
            })
        return render_to_response('account.html', variables)


@login_required(login_url="/login/")
def deposit_page(request):
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            transaction = CurrentAccount
            CurrentAccount.deposit(transaction, amount, request.user)
            return HttpResponseRedirect('/account/')
    else:
        form = DepositForm()
        account = get_account(request)
    variables = RequestContext(request, {
        'user': request.user,
        'deposit_form': form,
        'account': account
        })
    return render_to_response( 'deposit.html', variables )


@login_required(login_url="/login/")
def withdraw_page(request):
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            transaction = CurrentAccount
            CurrentAccount.withdraw(transaction, amount, request.user)
            return HttpResponseRedirect('/account/')
    else:
        form = WithdrawForm()
        account = get_account(request)
    variables = RequestContext(request, {
        'user': request.user,
        'withdraw_form': form,
        'account': account
        })
    return render_to_response( 'withdraw.html', variables )




@login_required(login_url="/login/")
def transfer_page(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            recipient = form.cleaned_data['recipient']
            accNumber = form.cleaned_data['accNumber']

            transaction = CurrentAccount
            CurrentAccount.transfer(transaction, request.user, amount, recipient, accNumber)
            return HttpResponseRedirect('/account/')
    else:
        form = TransferForm()
    account = get_account(request)
    variables = RequestContext(request, {
        'user': request.user,
        'transfer_form': form,
        'account': account
        })
    return render_to_response( 'transfer.html', variables )




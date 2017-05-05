
# banking/views.py - Views for the banking app
from banking.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


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


@login_required(login_url="login/")
def account_page(request):
    variables = RequestContext(request, { 'user': request.user })
    return render_to_response('account.html', variables)





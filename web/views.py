import json
from django.shortcuts import render
from django.contrib.auth import authenticate
from .clean_register import clean_data
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as logout_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from accounts.forms import RegisterFormSession
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import (HttpResponse ,
                        HttpResponseBadRequest,
                        HttpResponseRedirect)


User = get_user_model()
# Create your views here.
def home(request):
    context = {'title': 'Welcome to Chatbot', 'navtransparent': 1}
    return render(request, 'home.html', context)

@csrf_protect
def login(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/')
    context = {'title': 'Login'}
    
    return render(request, 'login.html', context)

def signup(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/')
    context = {'title': 'Signup'}
    return render(request, 'signup.html', context)

@csrf_protect
def loginsession(request):
    if request.method == 'POST':
        requestdata = json.loads(request.body.decode('utf-8'))
        email = requestdata.get('email', '').strip()
        password = requestdata.get('password', '').strip()
        if email and password:
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                auth_login(request, user)
                data = {'success': True}
            else:
                return HttpResponseBadRequest()
            return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponseBadRequest()


def register(request):
    if request.method == 'POST':
        requestdata = json.loads(request.body.decode('utf-8'))    
                          
        firstname  = requestdata.get('firstname', '').strip()
        lastname   = requestdata.get('lastname', '').strip()
        password    = requestdata.get('password', '').strip()
        email       = requestdata.get('email', '').strip()
        success , error = clean_data(firstname,lastname,password,email)
        if success:
            try:
                User.objects.create_user(email=email,
                            password=password, 
                            firstname=firstname, 
                            lastname=lastname)
                data = {'success': True}
            except:
                #Add error
                return  HttpResponseBadRequest()
            return HttpResponse(json.dumps(data), content_type='application/json')  # Redirect after POST
        return HttpResponseBadRequest(json.dumps(error), content_type='application/json')
    return HttpResponseBadRequest()
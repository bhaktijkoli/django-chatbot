from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
  
from django.http import HttpResponse  ,HttpResponseBadRequest
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import json
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def home(request):
    print(request.user.is_authenticated)
    context = {'title': 'Welcome to Chatbot', 'navtransparent': 1}
    return render(request, 'home.html', context)

@csrf_protect
def login(request):
    context = {'title': 'Login'}
    print(request.user.is_authenticated)
    return render(request, 'login.html', context)

def signup(request):
    print(request.user.is_authenticated)
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
            # Found a match
            print(user)
            if user is not None:
                # User is active
                   
                auth_login(request, user)
                data = {'success': True}

            else:
                data = {'success': False, 'error': 'Wrong username and/or password'}
            print(request.user.is_authenticated)
            return HttpResponse(json.dumps(data), content_type='application/json')

    # Request method is not POST or one of username or password is missing
    return HttpResponseBadRequest()
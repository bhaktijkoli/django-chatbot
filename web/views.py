from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
import json
# Create your views here.
def home(request):
    context = {'title': 'Welcome to Chatbot', 'navtransparent': 1}
    return render(request, 'home.html', context)

def login(request):
    context = {'title': 'Login'}
    print(request.user.is_authenticated)
    return render(request, 'login.html', context)

def signup(request):
    context = {'title': 'Signup'}
    return render(request, 'signup.html', context)

def loginsession(request):
    if request.method == 'POST':
        print(request.POST)
        login_form = AuthenticationForm(request, request.POST)
        response_data = {}
        if login_form.is_valid():
            response_data['result'] = 'Success!'
            response_data['message'] = 'You"re logged in'
        else:
            response_data['result'] = 'failed'
            response_data['message'] = 'You messed up'

        return HttpResponse(json.dumps(response_data), content_type="application/json")

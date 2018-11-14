from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'title': 'Welcome to Chatbot', 'navtransparent': 1}
    return render(request, 'home.html', context)

def login(request):
    context = {'title': 'Login'}
    return render(request, 'login.html', context)

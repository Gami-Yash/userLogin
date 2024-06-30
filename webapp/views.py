from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import loginModel,loginmodel2
from django.contrib.auth import login as auth_login ,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(username, password, email)
        if loginmodel2.objects.filter(username=username):
            print('User already exists')
        else:
            loginmodel2.objects.create(username=username, password=password,email=email)

    return render(request, 'newIndex.html')    
        

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request,user)
            print("hello",request.user.is_authenticated)
            # user_info = "Welcome, " + username
            return redirect('home/', {'user':user})
        else:
            print('error')
    return render(request, 'newIndex.html')

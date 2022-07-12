from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def createform(request) :
    if(request.method == 'POST') :
        print(request.POST)
        account_id = request.POST['user_ID']
        password = request.POST['user_PW1']
        name = request.POST['user_name']
        email = request.POST['user_email']
        phone = request.POST['user_phone']
        
        user = User.objects.create_user(name, email, password)
        user.account_id = account_id
        user.phone = phone
        user.save()

    return redirect('account')

def account(request) :
    return render(request, 'account.html')
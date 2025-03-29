from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login


def singup(request):
    if(request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/singup.html',{'form':form})

def loginPage(request):
    if (request.method == 'POST'):
        username  =  request.POST.get('username')
        password  =  request.POST.get('password')
       
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('dashbordEtudient')
        else:
                return render(request,'accounts/login.html',{'error':'les mot de passe ou email incorrect'})
    return render(request,'accounts/login.html')


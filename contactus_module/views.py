from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
# Create your views here.
def contactus_func (request):
    return render(request, 'contactus_module/contactus_page.html')
def user_register(request):
    if request.method=='Post':
        form_register=UserRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['username'],
                                     email=data['email'],
                                     first_name=data['firstname'],
                                     last_name=data['lastname'],
                                     password=data['password2'],
                                     )
            return redirect('home-module:home')

    else:
        form_register=UserRegisterForm()
    return render(request,'contactus_module/register.html',{'form_register':form_register})



def user_login(request):
    if request.method=='POST':
        form_login=UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            try:
                user=authenticate(request,usename=User.objects.get(email=data['user']),password=data['password'])
            except:
                user = authenticate(request, username=data['user'],
                                    password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('home-module:home')
    else:
        form_login=UserLoginForm()
    return render(request,'contactus_module/login.html',{'form_login':form_login})
def user_logout(request):
    logout(request)
    return  redirect('home-module:home')
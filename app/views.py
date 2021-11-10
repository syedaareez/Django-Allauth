from django.shortcuts import render
from .models import userProfile
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as ulogin
from .forms import UserForm

# Create your views here.
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'
    
def register(request):
    registered=False
    if request.method =='POST':
        user_form=UserForm(data=request.POST)
        

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
            return render(request,'home.html',{'registered':registered})
        else:
            return HttpResponse('Enter valid username and password!')
        return render(request,'home.html')
    else:
        return HttpResponse('Enter valid username and password! not POST')
    
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user=authenticate(request,username=username,password=password)

        if user:
            ulogin(request,user)
            print("user logged in")
            return render(request,'home.html')
        else:
            print('login failure')
            return HttpResponse('NO USER FOUND')
    else:
        return render(request,'home.html')
    
def logout(request):
    if(request.user):
        logout(request)
        return render(request,'home.html')
    else:
        return render(request,'home.html')

def signup(request):
    registered=False
    return render(request,'home.html',{'registered':registered})

def signin(request):
    registered=True
    return render(request,'home.html',{'registered':registered})
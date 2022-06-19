from django.views.generic.list import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from internapp.models import Attendence, TaskSubmit, task
from .forms import Attendenceform, RegistrationForm,TaskUploadForms
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
def SigninForm(request):
    if request.method =="POST":
        fm= RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Register Succesfully!!!')
            return redirect('loginpage')
    else:
        fm= RegistrationForm()    
    return render(request,'internapp/signin.html',{'form':fm})


def LoginForm(request):
    if request.method =='POST':
        fm = AuthenticationForm(request=request,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            reg = authenticate(username=uname,password=upass)
            if reg is not None:
                login(request,reg)
                messages.success(request,'Login Succesfully!!!')
                return redirect('homepage')
    fm = AuthenticationForm()
    return render (request, 'internapp/login.html',{'form':fm})
def HomePage(request):
    if request.user.is_authenticated:
        return render(request,'internapp/home.html',{'name':request.user})
    else:
        return redirect('loginpage')

def LogoutPage(request):
    logout(request)
    messages.success(request,'Message upload Succesfully!!!')
    return redirect('loginpage')


def AttendencePage(request):
    if request.method =='POST':
        fm= Attendenceform(request.POST)
        if fm.is_valid():
            att= fm.cleaned_data['attend']
            nm= fm.cleaned_data['name']
            dt = fm.cleaned_data['date']
            reg =Attendence (attend=att,name=nm,date=dt)
            reg.save()
            messages.success(request,'Attendece Done Succesfully!!!')
            return redirect('homepage')
    else:    
        fm = Attendenceform()
    return render(request,'internapp/attendence.html',{'form':fm})
def TaskView(request):
    return render (request,'internapp/task.html')



class TaskView(ListView):
    model = task

def TaskUpdateView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = TaskUploadForms(request.POST, request.FILES)
            if fm.is_valid():
                fn = fm.cleaned_data['fullname']
                tn = fm.cleaned_data['taskname']
                tf = fm.cleaned_data['taskfile']
                TaskSubmit(fullname=fn,taskname=tn,taskfile=tf).save()
                messages.success(request,'Message upload Succesfully!!!')
                return redirect('homepage')
        else:
            fm= TaskUploadForms()
        return render(request,'internapp/taskform.html',{'form':fm})
    else:
        return redirect('loginpage')

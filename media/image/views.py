from dataclasses import fields
from django.shortcuts import render

from formapp.models import UserList
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from.models import UserList
# Create your views here.
def MyRegisterationForm(request):
    if request.method =="POST":
        fm= RegistrationForm(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['Full_Name']
            pem = fm.cleaned_data['Email']
            ad = fm.cleaned_data['Address']
            gen = fm.cleaned_data['Gender']
            phn = fm.cleaned_data['Phone_Number']
            ppsw = fm.cleaned_data['Password']
            reg = UserList(Full_Name=fn,Email=pem,Address=ad,Gender=gen,Phone_Number=phn,Password=ppsw)
            reg.save()
            return HttpResponseRedirect('homepage')
            
    else:
        fm = RegistrationForm
    return render(request,'formapp/signin.html',{'form':fm})

def IndeView(request):
    return render(request,'formapp/index.html')
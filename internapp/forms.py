from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Attendence, TaskSubmit
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        


class Attendenceform(ModelForm):
    class Meta:
        model=Attendence
        fields= ['attend','name','date']
        widgets = {
            'name': forms.TextInput,
            'date': forms.DateInput,
        }

class TaskUploadForms(ModelForm):
    class Meta:
        model = TaskSubmit
        fields= '__all__'
        widgets = {
            'fullname':forms.TextInput,
            'taskname':forms.TextInput,
            'taskfile':forms.FileInput(attrs={'value':''})
        }
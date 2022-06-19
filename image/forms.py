from pydoc import render_doc
from django import forms
from .models import userModel
class UserForm(forms.ModelForm):
    class Meta:
        model = userModel
        fields = '__all__'
        widgets = {
            'Full_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'Phone_Number': forms.NumberInput(attrs={'class':'form-control'}),
            'Birth_Date': forms.DateInput(attrs={'class':'form-control'})
        }

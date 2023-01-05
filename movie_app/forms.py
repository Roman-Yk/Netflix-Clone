from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'name_input'}),
            'email': forms.EmailInput(attrs={'class':'email_input'})
        }







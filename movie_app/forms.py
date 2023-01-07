from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model=Customer
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'usernameinput', 'placeholder': 'Username'}),
            
        }







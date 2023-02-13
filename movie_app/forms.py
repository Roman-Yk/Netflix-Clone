from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model=Customer
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'usernameinput', 'placeholder': 'Username'}),
            
        }
        
class TariffForm(forms.Form):
    tariff = forms.CharField(widget=forms.RadioSelect(choices=TARIFF, attrs={'class': 'tariff'}))
    







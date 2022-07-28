from pyexpat import model
from attr import field
from django.core import validators
from django import forms

from .models import user

class studentreg(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name','mail','password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'mail' : forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value =True, attrs={'class':'form-control'}),
            }

         

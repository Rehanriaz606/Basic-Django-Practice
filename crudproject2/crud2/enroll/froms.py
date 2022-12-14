from attr import fields
from django import forms
from django.shortcuts import render
from matplotlib import widgets
from sqlalchemy import true
from .models import user

class studentregistration(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(attrs= {'class': 'form-control'}),
            'email' : forms.EmailInput(attrs= {'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value=true,attrs= {'class': 'form-control'}),
        }
from cProfile import label
from django import forms
from matplotlib import widgets
from requests import request
from .models import m_data
class f_data(forms.ModelForm):
    class Meta:
        model = m_data
        fields = ['h_id','h_name','h_email']
        labels = {"h_id":'ID','h_name':'Full Name','h_email':'Email Address'}
        



class hello(forms.Form):
    name = forms.CharField(required=True)
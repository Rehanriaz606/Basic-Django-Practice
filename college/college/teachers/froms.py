import email
from django import forms 


class subject(forms.Form):
    subject_name = forms.CharField()
    teacher_name = forms.CharField()
    email = forms.EmailField()
    salary = forms.IntegerField()

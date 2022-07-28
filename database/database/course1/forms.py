from django import forms

class course(forms.Form):
    stuid =  forms.IntegerField()
    stuname = forms.CharField(max_length=100)
    stuemail = forms.EmailField(max_length=100)
    stupassword = forms.CharField(max_length=100)
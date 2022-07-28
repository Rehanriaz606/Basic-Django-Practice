from django import forms

class f_computer(forms.Form):
    c_id = forms.IntegerField()
    c_model = forms.CharField()
    c_price = forms.IntegerField()
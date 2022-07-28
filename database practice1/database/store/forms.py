from django import forms

class pencil(forms.Form):
    p_id = forms.IntegerField()
    p_name = forms.CharField(max_length=100)
    p_price = forms.IntegerField()
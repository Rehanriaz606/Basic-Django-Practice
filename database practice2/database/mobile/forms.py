from django import forms

class oppo(forms.Form):
    o_id = forms.IntegerField(max_value=100)
    o_model = forms.CharField(max_length=100)
    o_price = forms.IntegerField(max_value=20)
    
from django import forms 

class Course(forms.Form):
    course_name = forms.CharField(max_length=30)
    course_code = forms.CharField()
    course_duration = forms.IntegerField()
    email = forms.EmailField()
    weight = forms.FloatField()
    percentage = forms.DecimalField()
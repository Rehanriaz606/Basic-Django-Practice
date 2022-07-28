from attr import fields
from django import forms
from .models import student

class Studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

class Teacherform(forms.ModelForm):
    class Meta(Studentform.Meta):
        fields = "__all__"

class Employeeform(forms.ModelForm):
    class Meta(Studentform.Meta):
        fields = '__all__'

    

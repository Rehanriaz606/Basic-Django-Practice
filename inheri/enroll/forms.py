from attr import fields
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = ['name','school_id','age']
        fields = '__all__'
        '''exclude = ['age']'''


class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = ['name','school_id','age']


class EmployeesForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = '__all__'
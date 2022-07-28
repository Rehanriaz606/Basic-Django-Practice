from re import template
from django.http import HttpResponse
from django.shortcuts import render

from .forms import Studentform
from .models import student
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def student_view(request):
    stu = student.objects.all()
    return render(request,'student.html',{'abc':stu})

class teacher_view(View):
    def get(self,request):
        return render(request,'teacher.html')

class Employee_view(TemplateView):
    template_name = 'employee.html'




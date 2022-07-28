from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .forms import EmployeesForm, StudentForm
from .forms import TeacherForm

from django.views.generic.base import TemplateView

# Create your views here.

from django.views import View


'''class views 
Base Class Based View - Base View- - - - view,template view redirect view 

Generic Class Geneic View - Genric View
'''

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Asad'
        context['address'] = 'Karachi'
        context['Profession'] = 'Cricket'
        return context





def student_view(request):
    if request.method == 'POST':
        sf = StudentForm(request.POST)
        if sf.is_valid():
            sf.save()
        sf = StudentForm()
    else:
        sf = StudentForm()
    stud = Student.objects.all()
    return render(request, 'student.html',{'abc':sf})
        
class MyView(View):
    name = 'Rehan'
    def get(self,request):
        
        return HttpResponse(self.name)
        #return render(request,'index.html')
# t = Teacher()

class Teacher_view(View):
    name = 'Waqar'
    def get(self,request):
        tform = TeacherForm
        return render(request,'index.html',{'form':tform})

class Employee_view(View):
    name = 'Akbar'
    def get(self,request):
        eform = EmployeesForm()
        return render(request,'employee.html',{'form':eform})
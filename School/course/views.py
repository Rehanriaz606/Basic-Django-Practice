from django.shortcuts import render
from .forms import Course
# Create your views here.
def course_view(request):
    cr = Course()
    return render(request,'index.html',{'abc':cr})
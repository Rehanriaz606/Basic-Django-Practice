from django.shortcuts import render
from numpy import delete
from . forms import course
from .models import student
# Create your views here.
def course_view(request):
    if request.method == 'POST':
        ab = course(request.POST)
        if ab.is_valid():
            stu_id = ab.cleaned_data['stuid']
            stu_name = ab.cleaned_data['stuname']
            stu_email = ab.cleaned_data['stuemail']
            stu_password = ab.cleaned_data['stupassword']
            
            reg = student(pk=6,stuid=stu_id,stuname=stu_name,stuemail=stu_email,stupassword=stu_password)
            reg.save()
            #dele = student(pk=10)
            #dele.delete()
    else:
       ab = course()
    return render (request, 'index.html',{'abc':ab})
    
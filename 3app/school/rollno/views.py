from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rehan(request):
    rehan = {'name':'rehan','rollno':'21'}
    return render(request,'rollno/rollno.html',rehan)
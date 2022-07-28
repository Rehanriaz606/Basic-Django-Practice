from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rehan(request):
    rehan = {'name':'rehan','subject':'physics'}
    return render(request,'subject/subject.html',rehan)
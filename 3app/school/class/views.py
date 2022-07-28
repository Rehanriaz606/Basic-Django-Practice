from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rehan(request):
    rehan ={'name':'rehan','class':'mcs'}
    return render(request,'class/class.html',rehan)
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def half(request):
     return render(request,'no5half.html')

def full(request):
    return render(request,('no5full.html'))

def mid(request):
    return render(request,('no5mid.html'))
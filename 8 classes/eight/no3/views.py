from ast import Return
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def half(request):
    return render(request,'no3half.html')

def mid(request):
    return render(request,'no3mid.html')

def full(request):
    return render(request,'no3full.html')
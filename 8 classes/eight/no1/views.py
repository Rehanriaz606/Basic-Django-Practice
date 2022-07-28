from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def half(request):
    return render (request,'no1.html')

def mid(request):
    return render(request,'no1mid.html')

def full(request):
    return render (request,'no1full.html') 
    
    
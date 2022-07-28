from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def half(request):
    return render (request,'no2half.html')

def mid(request):
    return render (request,'no2mid.html')

def full(request):
    return render (request,'no2full.html')
    
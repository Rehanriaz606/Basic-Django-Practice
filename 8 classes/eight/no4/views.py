from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def half(request):
    return render(request,'no4half.html')

def full(request):
    return render(request,'no4full.html')

def mid(request):
    return render(request,'no4mid.html')
    
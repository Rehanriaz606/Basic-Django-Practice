from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def details(request):
    return HttpResponse("phone details")

def home(request):
    return HttpResponse('phone home')
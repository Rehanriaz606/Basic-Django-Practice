from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Massages Home')

def details(request):
    return HttpResponse('Massages Details')
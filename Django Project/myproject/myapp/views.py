from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sympy import hn1
def django_project (request):
    return HttpResponse("Django Page")

def home (request):
    return HttpResponse('<h1>Home Page</h1>')
    
from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ('Home Page app2')

def details(request):
    return HttpResponse ('Details app2')
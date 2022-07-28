from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse ('Alarm Home')
def details(request):
    return HttpResponse('Alarm Details')
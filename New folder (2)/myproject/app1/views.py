from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'app1.html')

def details(request):
    return HttpResponse('Details app1')
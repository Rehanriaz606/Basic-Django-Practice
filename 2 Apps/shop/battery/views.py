from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def price(request):
    return render(request,'battery/b_price.html')
def color(request):
    return render(request,'battery/b_color.html')
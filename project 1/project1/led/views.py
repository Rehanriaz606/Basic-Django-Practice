from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def huawei(request):
    huawei = {'name':'huawei','price':'340$','inches':'32'}
    return render(request,'products.html',huawei)

def samsung(request):
    samsung = {'name':'samsung','price':'430$','inches':'50'}
    return render(request,'led/products.html',samsung)

def oriant(request):
    oriant = {'name':'oriant','price':'650$','inches':'100'}
    return render(request,'products.html',oriant)
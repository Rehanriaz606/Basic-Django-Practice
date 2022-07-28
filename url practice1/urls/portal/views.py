from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'Hello: This is home page'})

def contact(request):
    return render(request,'index.html',{'Hello: This is contact page'})

def about(request):
    return render(request,'index.html',{'Hello: This is about us page'})

def career(request):
    return render(request,'index.html',{'Hello: This is career page'})
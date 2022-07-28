from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

# Password Change
# Password Reset
# Login
# Logout


def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:        
        form = UserCreationForm()
    return render(request,'index.html',{'form':form})
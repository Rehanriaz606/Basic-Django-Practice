from django.shortcuts import render
from .forms import f_computer
from .models import m_computer
# Create your views here.
def computer_view(request):
    if request.method == 'POST':
        com = f_computer(request.POST)
        if com.is_valid():
            com.save()
    else:
        com = f_computer()
    return render(request,'index.html',{'ab':com})
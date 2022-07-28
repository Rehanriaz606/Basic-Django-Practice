
import email
from django.shortcuts import render
from .models import m_data
from .forms import f_data
# Create your views here.
def hostel_view(request):
    if request.method == 'POST':
        h= f_data(request.POST)
        if h.is_valid():
            h.save()

            
            '''            idd= h.cleaned_data['h_id']
            name= h.cleaned_data['h_name']
            mail=h.cleaned_data['h_email']
            reg = m_data(h_id=idd,h_name=name,h_email=mail)
            reg.save()'''

    else:
        h=f_data()
    return render(request,'index.html',{'abc':h})        

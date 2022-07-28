from urllib import request
from django.shortcuts import render
from .forms import pencil
from .models import m_pencil
# Create your views here.
def store_view(request):
    if request.method == 'POST':
        p = pencil(request.POST)
        if p.is_valid():
            id = p.cleaned_data['p_id']
            name = p.cleaned_data['p_name']
            price = p.cleaned_data['p_price']
        reg = m_pencil(p_id = id,p_name=name,p_price=price)
        reg.save()

    else:
        p = pencil()
    return render(request,'index.html',{'abc':p})
        


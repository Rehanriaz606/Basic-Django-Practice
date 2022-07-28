from django.shortcuts import render
from .models import omobile
from .forms import oppo
# Create your views here.
def mobile_view(request):
    if request.method== 'POST':
        om = oppo(request.POST)
        if om.is_valid():
            id = om.cleaned_data['o_id']
            name = om.cleaned_data['o_model']
            price = om.cleaned_data['o_price']

            reg = omobile(o_id= id,o_model=name,o_price=price)
            reg.save()

    else:
            om = oppo
    return render(request,'index.html',{'abc':om})

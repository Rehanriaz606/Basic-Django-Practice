from django.shortcuts import render
from . froms import subject
# Create your views here.
def teachers_view(request):
    ahmed = subject()
    return render(request, 'index.html',{'abc':ahmed})

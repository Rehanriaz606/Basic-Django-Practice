from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . models import movies


# Create your views here.
def index(request):
    #global moviee
    moviee = movies.objects.all()
    return render(request, 'movie/index.html',{'movies':moviee})

def detail(request,movie_id):
    movie= get_object_or_404(movies,pk=movie_id)
    return render(request, "movie/detail.html",{'movies':movie})
   
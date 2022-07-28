from urllib.parse import urlparse
from django.urls import path
from . import views
urlpatterns = [
    
    path('price/',views.price),
    path('color/',views.color),
]

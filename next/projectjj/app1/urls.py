from django.urls import path
from . import views

urlpatterns = [
    path('gallery/',views.gallery),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact)


]
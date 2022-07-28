from django import views
from django.urls import path
from no2 import views

urlpatterns = [
    path ('half/',views.half),
    path ('mid/',views.mid),
    path ('full/',views.full),
]

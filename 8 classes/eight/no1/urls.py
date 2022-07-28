from django.urls import path
from . import views


urlpatterns = [
    path('half/',views.half),
    path('mid/',views.mid),
    path('full/',views.full),
]

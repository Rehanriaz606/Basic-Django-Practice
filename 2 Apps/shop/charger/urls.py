from django.urls import path
from . import views
urlpatterns = [
    path('lenovo/',views.lenovo),
    path('hp/',views.hp),
    path('dell/',views.dell),
    path('toshiba/',views.toshiba),
    path('macbook/',views.macbook),
]

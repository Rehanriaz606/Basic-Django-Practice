from django.urls import path
from . import views

urlpatterns = [
    path('samsung/',views.samsung),
    path('oriant/',views.oriant),
    path('huawei/',views.huawei),
]

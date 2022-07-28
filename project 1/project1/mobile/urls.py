from django.urls import path
from . import views

urlpatterns = [
    path('samsung/',views.samsung),
    path('huawei/',views.huawei),
    path('oppo/',views.oppo)
]

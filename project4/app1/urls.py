from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('home1/', views.home1),
    path('set/', views.setcookie),
    path('get/', views.getcookie),
    path('del/', views.delcookie),
    path('set_s/', views.setsession),
    path('get_s/', views.getsession),
    path('del_s/', views.delsession),
]

from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home,),
    path("home1/", views.home1,),
    path("home2", views.home2,),
    # path("", views.home3,),
    path("", views.Myview.as_view()),
]

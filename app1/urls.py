from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sirr/", views.sirr, name="sirr"),
    path("eodrisk/", views.eodrisk, name="eodrisk"),
]
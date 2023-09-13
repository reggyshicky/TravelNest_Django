from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("flightdetails/<int:pk>", views.flightdetails, name="flightdetails"),
]
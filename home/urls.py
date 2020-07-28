from django.urls import path

from . import views

urlpatterns = [
    path('', views.PetView.as_view()),
]
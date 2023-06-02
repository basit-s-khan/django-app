from django.urls import path
from . import views


urlpatterns = [
    path("" , views.main , name='main'),
    path('first/', views.first , ),
    path('testing/', views.testing , name= 'testing'),
    path("members/" , views.hello , name='hello'),
    path("members/details/<int:slug>" , views.details ,name="details")
]
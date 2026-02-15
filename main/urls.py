from django.urls import path
from  main.views import register

urlpatterns = [
    path('',register),
]


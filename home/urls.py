from django.urls import path
from . import views

# The url for my products app
urlpatterns = [
    path('', views.index, name='home')
]

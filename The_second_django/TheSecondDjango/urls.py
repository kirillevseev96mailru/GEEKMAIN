from django.urls import path
from .views import *


urlpatterns = [
    path('about/', about),
    path('index/', index),
    path('all_the_time/<str:name>', all_the_time),
]
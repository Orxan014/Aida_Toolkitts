from django.urls import path
from .views import *

urlpatterns = [
    path('calendar/',calendar , name='calendar'),
    path('add_post/', add_post, name='add_post')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('unauthorizedaccess', unauthorizedaccess, name='unauthorizedaccess'),
    path('illegalactivity', illegalactivity, name='illegalactivity'),
    
    
]

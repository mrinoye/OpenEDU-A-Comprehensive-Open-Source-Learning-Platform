from django.urls import path
from .views import *

urlpatterns = [
    path('', departments, name='departments'),
    path('courses', courses, name='courses'),
    path('students', students, name='students'),
    
]

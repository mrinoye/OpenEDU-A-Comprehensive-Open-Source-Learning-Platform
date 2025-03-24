from django.urls import path
from .views import *

urlpatterns = [
    
    path('department=<int:id>/', deptcourses, name='deptcourses')
    
]

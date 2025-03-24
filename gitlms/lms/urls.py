from django.urls import path
from .views import *

urlpatterns = [
    
    path('department=<int:id>/', deptcourses, name='deptcourses'),
    path('department=<int:dept_id>/course=<int:course_id>', course_facs, name='course_facs')
]

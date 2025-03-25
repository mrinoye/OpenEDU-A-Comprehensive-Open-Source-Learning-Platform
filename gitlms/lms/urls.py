from django.urls import path
from .views import *

urlpatterns = [
    
    path('department=<int:id>/', deptcourses, name='deptcourses'),
    path('department=<int:dept_id>/course=<int:course_id>', course_facs, name='course_facs'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>',fac_lecs, name='fac_lecs'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures',lec_slides, name='lec_slides'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures/slide=<int:slide_id>',show_pdf, name='show_pdf')
]

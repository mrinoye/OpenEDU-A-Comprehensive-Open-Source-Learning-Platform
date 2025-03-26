from django.urls import path
from .views import *

urlpatterns = [
    path('', departments, name='departments'),
    path('courses', courses, name='courses'),
    path('department=<int:id>/', deptcourses, name='deptcourses'),
    path('department=<int:dept_id>/course=<int:course_id>', course_facs, name='course_facs'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>',fac_lecs, name='fac_lecs'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures',lec_slides, name='lec_slides'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures/slide=<int:slide_id>',show_pdf, name='show_pdf'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures/videos', lec_videos, name='lec_videos'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures/videos/video=<int:video_id>', show_video, name='show_video'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures/notes', lec_notes, name='lec_notes'),
    path('department=<int:dept_id>/course=<int:course_id>/faculty=<int:fac_id>/Lectures/notes/note=<int:note_id>', show_note, name='show_note')
]
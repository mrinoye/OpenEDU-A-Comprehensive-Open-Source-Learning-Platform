from django.urls import path
from .views import *

urlpatterns = []

pages=[path('', home, name='home'),
    path('courses', courses, name='courses'),
    path('students', students, name='students'),
    path('appoint', appoint, name='appoint'),]

functionalities=[ path('changerole/<int:userid>/<str:role>/', changerole, name='changerole')]

urlpatterns+=pages
urlpatterns+=functionalities
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Department,Course,Faculty
from django.conf import settings


# Create your views here.

#for Courses inside a Department
@login_required
def deptcourses(request,id):
    department=Department.objects.get(id=id)
    courses = Course.objects.filter(department=department).order_by('course_name')

    context={'name':request.user.username,'courses':courses , 'department': department}
    return render(request,'deptcourses.html',context)



#for faculties inside a Course
@login_required
def course_facs(request, dept_id, course_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculties = Faculty.objects.filter(course=course)
    context = {'department': department, 'faculties': faculties,'course':course}
    return render(request, 'faculty.html', context)



#for lectures inside a Faculty
@login_required
def fac_lecs(request, dept_id, course_id,fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    context = {'department': department, 'faculty': faculty,'course':course,'MEDIA_URL':settings.MEDIA_URL}
    return render(request, 'lectures.html', context)

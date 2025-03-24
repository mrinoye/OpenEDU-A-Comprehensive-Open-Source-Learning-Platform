from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Department,Course,Faculty
# Create your views here.
@login_required
def deptcourses(request,id):
    department=Department.objects.get(id=id)
    courses = Course.objects.filter(department=department).order_by('course_name')

    context={'name':request.user.username,'courses':courses , 'department': department}
    return render(request,'deptcourses.html',context)

@login_required
def course_facs(request, dept_id, course_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculties = Faculty.objects.filter(course=course)
    print(faculties)
    context = {'department': department, 'faculties': faculties,'course':course}
    return render(request, 'faculty.html', context)
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Department,Course

# Create your views here.
@login_required
def deptcourses(request,id):
    department=Department.objects.get(id=id)
    courses = Course.objects.filter(department=department).order_by('course_name')

    context={'name':request.user.username,'courses':courses}
    return render(request,'deptcourses.html',context)

from django.shortcuts import redirect,redirect, get_object_or_404
from .models import *
from accounts.models import User
from django.contrib import messages


def delete_dept(request,dept_id):
    if (request.user.role!='master')&(request.user.department!=dept_id):
        return redirect('illegalactivity')
    if request.user.role=='master':
        department = Department.objects.get(id=dept_id)
        department.delete()
        messages.success(request, "Department has been deleted")
    else:
        print("request sent")
    
    return redirect('departments')

def delete_course(request,dept_id,course_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
        return redirect('illegalactivity')
    department=get_object_or_404(Department,id=dept_id)
    course = get_object_or_404(Course, id=course_id)
    if((request.user.role=='master')or(request.user.department== dept_id)):
        course.delete()
        messages.success(request, "Course has been deleted")
    else:
        print("request sent")
    return redirect('deptcourses',department.id)




def delete_fac(request,dept_id,course_id,fac_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
         return redirect('illegalactivity')
    faculty=get_object_or_404(Faculty,id=fac_id)
    faculty.delete()
    messages.success(request, "Faculty has been deleted")
    return redirect('course_facs',dept_id,course_id)



def delete_slide(request,dept_id,course_id,fac_id,slide_id):
    return redirect('lec_slides')

def delete_note(request,dept_id,course_id,fac_id,note_id):
    return redirect('lec_notes')

def delete_video(request,dept_id,course_id,video_id):
    return redirect('lec_videos')




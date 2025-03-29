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
    slide=get_object_or_404(Slide, id=slide_id)
    if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
        slide.delete()
        messages.success(request, "Slide has been deleted")
    else:
        messages.success(request, "Request Sent")
    return redirect('lec_slides',dept_id, course_id, fac_id)



def delete_note(request,dept_id,course_id,fac_id,note_id):
    note=get_object_or_404(Note, id=note_id)
    if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
        note.delete()
        messages.success(request, "Note has been deleted")
    else:
        messages.success(request, "Request Sent")
    return redirect('lec_notes',dept_id, course_id, fac_id)


def delete_video(request,dept_id,course_id,fac_id,video_id):
    video=get_object_or_404(Video, id=video_id)
    if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
        video.delete()
        messages.success(request, "Video has been deleted")
    else:
        messages.success(request, "Request Sent")
    return redirect('lec_videos',dept_id, course_id, fac_id)




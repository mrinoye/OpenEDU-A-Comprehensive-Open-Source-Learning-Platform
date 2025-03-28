from django.shortcuts import redirect ,redirect, get_object_or_404
from .models import *
from accounts.models import User
from django.contrib import messages




def update_dept(request, dept_id):
    if (request.user.role!='master')&(request.user.department!=dept_id):
        return redirect('illegalactivity')
    department = get_object_or_404(Department, id=dept_id)
    
    if request.method == 'POST':
        dept_name = request.POST.get('departmentName')
        dept_desc = request.POST.get('departmentDescription')
        dept_image = request.FILES.get('departmentImage')
    if request.user.role=='master':   
        if dept_name:
            department.name = dept_name
        if dept_desc:
            department.description = dept_desc
        if dept_image:
            department.image= dept_image

        department.save()
        messages.success(request, "Department has been updated")
        return redirect('departments')
    else:
        print("request sent")
    return redirect('departments')


def update_course(request,dept_id,course_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
        return redirect('illegalactivity')
    department=get_object_or_404(Department,id=dept_id)
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course_code = request.POST.get('courseCode')
        course_name = request.POST.get('courseName')
        course_desc = request.POST.get('courseDescription')
        course_image = request.FILES.get('courseImage')
    if((request.user.role=='master')or(request.user.department== dept_id)):
        if course_code:
            course.course_code=course_code
        if course_name:
            course.course_name=course_name
        if course_desc:
            course.description=course_desc
        if course_image:
            course.image=course_image
        course.save()
        messages.success(request, "Course has been updated")
    else:
        print("request sent")
    return redirect('deptcourses',department.id)




def update_fac(request,dept_id,course_id,fac_id):
    faculty=get_object_or_404(Faculty, id=fac_id)
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
         return redirect('illegalactivity')
    if request.method == 'POST':
        faculty_name = request.POST.get('facultyName')
        position = request.POST.get('position')
        image= request.FILES.get('facultyImage')
    if faculty_name:
        faculty.name = faculty_name
    if position:
        faculty.position = position
    if image:
        faculty.image = image
    faculty.save()
    messages.success(request, "Faculty has been updated")
    return redirect('course_facs',dept_id,course_id)

def update_slide(request,dept_id,course_id,fac_id,slide_id):
    slide=get_object_or_404(Slide, id=slide_id)
    if request.method == 'POST':
        slide_name = request.POST.get('slideName')
        slide_content = request.FILES.get('slideContent')
        if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
            if slide_name:
                slide.name= slide_name
            if slide_content:
                slide.content=slide_content
            slide.save()
            messages.success(request, "Slide has been updated")
        else:
            messages.success(request, "Request sent")
    return redirect('lec_slides',dept_id, course_id, fac_id)
   

def update_note(request,dept_id,course_id,fac_id,note_id):
    return redirect('lec_notes')

def update_video(request,dept_id,course_id,video_id):
    return redirect('lec_videos')



from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from accounts.models import User
from django.http import HttpResponse
from django.contrib import messages


# Add Department
def add_dept(request):
    if (request.user.role!='master'):
        return redirect('illegalactivity')
    if request.method == 'POST':
        dept_name = request.POST.get('departmentName')
        dept_desc = request.POST.get('departmentDescription')
        dept_image = request.FILES.get('departmentImage')
        if(dept_name  ):
            department=Department.objects.create( name=dept_name   )
            if(dept_image):
                department.image=dept_image
            if( dept_desc):
                department.description=dept_desc
        department.save()
        messages.success(request, "Department has been added")
        return redirect('departments')
    
    return redirect('departments')

# Add Course
def add_course(request, dept_id):
    if (request.user.role!='master')and(request.user.department!= dept_id):
        return redirect('illegalactivity')
    department=get_object_or_404(Department,id=dept_id)
    if request.method == 'POST':
        course_code = request.POST.get('courseCode')
        course_name = request.POST.get('courseName')
        course_desc = request.POST.get('courseDescription')
        course_image = request.FILES.get('courseImage')
        if(course_code and course_name):
            course=Course.objects.create(course_code=course_code, course_name=course_name,department=department)
            if course_desc:
                course.description=course_desc
            if course_image:
                course.image=course_image
        course.save()
        messages.success(request, "Course has been added")
    return redirect('deptcourses',department.id)



# Add Faculty
def add_fac(request, dept_id, course_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
        return redirect('illegalactivity')
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        faculty_name = request.POST.get('facultyName')
        position = request.POST.get('position')
        image= request.FILES.get('facultyImage')
        if(faculty_name and position):
            faculty=Faculty.objects.create(name=faculty_name, position=position,course=course)
            if image:
                faculty.image=image
            faculty.save()
        messages.success(request, "Faculty has been added")
    return redirect('course_facs',dept_id,course_id)
    
 
# Add Slide
def add_slide(request, dept_id, course_id, fac_id):
    faculty=get_object_or_404(Faculty, id=fac_id)
    if request.method == 'POST':
        slide_name = request.POST.get('slideName')
        slide_content = request.FILES.get('slideContent')
        if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
            Slide.objects.create(name=slide_name, content=slide_content, faculty=faculty)
            messages.success(request, "Slide has been added")
        else:
            messages.success(request, "Request sent")
    return redirect('lec_slides',dept_id, course_id, fac_id)
    

# Add Note
def add_note(request, dept_id, course_id, fac_id):
    if request.method == 'POST':
        faculty=get_object_or_404(Faculty, id=fac_id)
    if request.method == 'POST':
        note_name = request.POST.get('noteName')
        note_content = request.FILES.get('noteContent')
        if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
            Note.objects.create(name=note_name, content=note_content, faculty=faculty)
            messages.success(request, "Note has been added")
        else:
            messages.success(request, "Request sent")
    return redirect('lec_notes',dept_id, course_id,fac_id)

# Add Video
def add_video(request, dept_id, course_id,fac_id):
    if request.method == 'POST':
        faculty=get_object_or_404(Faculty, id=fac_id)
    if request.method == 'POST':
        video_name = request.POST.get('videoName')
        video_content = request.FILES.get('videoContent')
        if (request.user.role=='master')or(request.user.department== dept_id)or(request.user.course== course_id):
            Video.objects.create(name=video_name, content=video_content, faculty=faculty)
            messages.success(request, "Video has been added")
        else:
            messages.success(request, "Request sent")
    return redirect('lec_videos',dept_id, course_id,fac_id)

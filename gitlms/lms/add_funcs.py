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
def add_slide(request, dept_id, course_id, fac_id, slide_id):
    
    if request.method == 'POST':
        slide_name = request.POST.get('slideName')
        slide_content = request.FILES.get('slideContent')
        # Save the new slide (assuming you have a model for it)
        Slide.objects.create(name=slide_name, content=slide_content, faculty_id=fac_id)
        return redirect('lec_slides')
    return render(request, 'slideModal.html')

# Add Note
def add_note(request, dept_id, course_id, fac_id, note_id):
    if request.method == 'POST':
        note_name = request.POST.get('noteName')
        note_content = request.FILES.get('noteContent')
        # Save the new note (assuming you have a model for it)
        Note.objects.create(name=note_name, content=note_content, faculty_id=fac_id)
        return redirect('lec_notes')
    return render(request, 'noteModal.html')

# Add Video
def add_video(request, dept_id, course_id,fac_id, video_id):
    if request.method == 'POST':
        video_name = request.POST.get('videoName')
        video_content = request.FILES.get('videoContent')
        # Save the new video (assuming you have a model for it)
        Video.objects.create(name=video_name, content=video_content, course_id=course_id)
        return redirect('lec_videos')
    return render(request, 'videoModal.html')

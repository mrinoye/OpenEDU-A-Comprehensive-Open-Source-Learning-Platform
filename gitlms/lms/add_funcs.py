from django.shortcuts import render, redirect
from .models import *
from accounts.models import User
from django.http import HttpResponse

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
        return redirect('departments')
    
    return redirect('departments')

# Add Course
def add_course(request, dept_id, course_id):
    if request.method == 'POST':
        course_code = request.POST.get('courseCode')
        course_name = request.POST.get('courseName')
        course_desc = request.POST.get('courseDescription')
        # Save the new course (assuming you have a model for it)
        Course.objects.create(code=course_code, name=course_name, description=course_desc, department_id=dept_id)
        return redirect('depa_course')
    return render(request, 'courseModal.html')

# Add Faculty
def add_fac(request, dept_id, course_id, fac_id):
    if request.method == 'POST':
        faculty_name = request.POST.get('facultyName')
        position = request.POST.get('position')
        # Save the new faculty (assuming you have a model for it)
        Faculty.objects.create(name=faculty_name, position=position, department_id=dept_id, course_id=course_id)
        return redirect('course_facs')
    return render(request, 'facultyModal.html')

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

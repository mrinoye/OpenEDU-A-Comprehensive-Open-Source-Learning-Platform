from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Department,Course,Faculty,Slide,Video,Note
from django.conf import settings



@login_required
# Create your views here.
def departments(request):
    departments=Department.objects.all().order_by('name')
    context={'name':request.user.username,'departments':departments}

    return render(request,"departments.html",context)

@login_required
def courses(request):
    courses = Course.objects.all().order_by('course_name')

    context={'name':request.user.username,'courses':courses}

    return render(request,"courses.html",context)

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

#for slides inside a lecture
@login_required
def lec_slides(request,dept_id, course_id,fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    slides=Slide.objects.filter(faculty=faculty)
    context = {'department': department, 'faculty': faculty,'course':course,'slides':slides}
    
    return render(request,"slides.html",context)


#To view the pdf
@login_required
def show_pdf(request,dept_id, course_id,fac_id,slide_id):
    
    slide=Slide.objects.get(id=slide_id)
    context = {'slide':slide}
    
    return render(request,"pdfViewer.html",context)

# For videos inside a lecture
@login_required
def lec_videos(request, dept_id, course_id, fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    videos = Video.objects.filter(faculty=faculty)
    context = {'department': department, 'faculty': faculty, 'course': course, 'videos': videos}
    return render(request, "videos.html", context)

# To view a video
@login_required
def show_video(request, dept_id, course_id, fac_id, video_id):
    video = Video.objects.get(id=video_id)
    context = {'video': video}
    return render(request, "videoViewer.html", context)

# For notes inside a lecture
@login_required
def lec_notes(request, dept_id, course_id, fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    notes = Note.objects.filter(faculty=faculty)
    context = {'department': department, 'faculty': faculty, 'course': course, 'notes': notes}
    return render(request, "notes.html", context)

# To view a note
@login_required
def show_note(request, dept_id, course_id, fac_id, note_id):
    note = Note.objects.get(id=note_id)
    context = {'note': note}
    return render(request, "noteViewer.html", context)
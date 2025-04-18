
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Department,Course,Faculty,Slide,Video,Note
from django.conf import settings
from .contentViewers import *
from .queryProxy import QueryCacheProxy

@login_required
def departments(request):
    department_proxy = QueryCacheProxy(request.user)
    departments = department_proxy.get_departments()  # Fetch departments via the proxy
    
    # Determine the visibility of the modal and button based on the user's role
    showDeptModal = (request.user.role == 'master')
    showUpdateDeptModal = (request.user.role == 'master')
    showAddButton = (request.user.role == 'master')
    
    # Prepare the context with user and departments information
    context = {
        'name': request.user.username,
        'departments': departments,
        'showDeptModal': showDeptModal,
        'showUpdateDeptModal': showUpdateDeptModal,
        'showAddButton': showAddButton
    }

    # Render the departments page with the context
    return render(request, "lms/departments.html", context)

@login_required
def courses(request):
    courses = Course.objects.all().order_by('course_name')

    context={'name':request.user.username,'courses':courses}

    return render(request,"courses.html",context)

# Create your views here.

#for Courses inside a Department
@login_required
def deptcourses(request,id):
    course_proxy = QueryCacheProxy(request.user)
    department = Department.objects.get(id=id)
    courses = course_proxy.get_courses(department)  # Fetch departments via the pr
    showAddButton=(request.user.role=='master')or(request.user.department==department.id)
    showUpdateCourseModal=(request.user.role=='master')or(request.user.department==department.id)
    showCourseModal=(request.user.role=='master')or(request.user.department==department.id)
    context={'name':request.user.username,'courses':courses , 'department': department,
             'showCourseModal':showCourseModal,'showUpdateCourseModal':showUpdateCourseModal,'showAddButton':showAddButton}
    return render(request,'lms/deptcourses.html',context)




#for faculties inside a Course
@login_required
def course_facs(request, dept_id, course_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculties = Faculty.objects.filter(course=course)
    showFacultyModal=(request.user.role=='master')or(request.user.department==department.id)or(request.user.course==course.id)
    showUpdateFacultyModal=(request.user.role=='master')or(request.user.department==department.id)or(request.user.course==course.id)
    showAddButton=(request.user.role=='master')or(request.user.department==department.id)or(request.user.course==course.id)
    context = {'department': department, 'faculties': faculties,'course':course,
               'showFacultyModal':showFacultyModal,'showUpdateFacultyModal':showUpdateFacultyModal,'showAddButton':showAddButton}
    return render(request, 'lms/faculty.html', context)



#for lectures inside a Faculty
@login_required
def fac_lecs(request, dept_id, course_id,fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    context = {'department': department, 'faculty': faculty,'course':course,'MEDIA_URL':settings.MEDIA_URL}
    return render(request, 'lms/lectures.html', context)

#for slides inside a lecture
@login_required
def lec_slides(request,dept_id, course_id,fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    slides=Slide.objects.filter(faculty=faculty)
    context = {'department': department, 'faculty': faculty,'course':course,'slides':slides,'showSlideModal':True,'showUpdateSlideModal':True,'showAddButton':True}
    
    return render(request,"lms/slides.html",context)



# For videos inside a lecture
@login_required
def lec_videos(request, dept_id, course_id, fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    videos = Video.objects.filter(faculty=faculty)
    context = {'department': department, 'faculty': faculty, 'course': course, 'videos': videos,'showVideoModal':True,'showUpdateVideoModal':True,'showAddButton':True}
    return render(request, "lms/videos.html", context)



# For notes inside a lecture
@login_required
def lec_notes(request, dept_id, course_id, fac_id):
    department = Department.objects.get(id=dept_id)
    course = Course.objects.get(id=course_id)
    faculty = Faculty.objects.get(id=fac_id)
    notes = Note.objects.filter(faculty=faculty)
    context = {'department': department, 'faculty': faculty, 'course': course, 'notes': notes,'showNoteModal':True,'showUpdateNoteModal':True,'showAddButton':True}
    return render(request, "lms/notes.html", context)


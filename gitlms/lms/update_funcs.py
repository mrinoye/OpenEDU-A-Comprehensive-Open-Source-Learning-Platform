from django.shortcuts import redirect ,redirect, get_object_or_404
from .models import *
from accounts.models import User
from django.contrib import messages
from .Observer import Subject ,MessageObserver
from notifications.models import Notification
from django.db.models import Q


messageObserver=MessageObserver()
subject=Subject()
subject.attach(messageObserver)

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
        subject.notify(request, "Department has been updated")
        return redirect('departments')
    else:
        subject.notify(request, "Request sent")
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
        subject.notify(request, "Course has been updated")
    else:
        subject.notify(request, "Request sent")
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
    subject.notify(request, "Faculty has been updated")
    return redirect('course_facs',dept_id,course_id)

# Update Slide
def update_slide(request, dept_id, course_id, fac_id, slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    if request.method == 'POST':
        slide_name = request.POST.get('slideName')
        slide_content = request.FILES.get('slideContent')
        if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
            if slide_name:
                slide.name = slide_name
            if slide_content:
                slide.content = slide_content
            slide.save()
            subject.notify(request, "Slide has been updated")
        else:
            # Creating a temporary Slide and sending notification
            temp_slide = temp_Slide.objects.create(name=slide_name, content=slide_content, faculty=slide.faculty)
            notification = Notification.objects.create(
                message=f"{request.user.first_name} {request.user.last_name} wants to update a slide",
                sender=request.user,
                type="update",
                content_type="slide",
                content_id=temp_slide.id,
                real_content_id=slide.id
            )
            receivers = User.objects.filter(Q(role='master') | Q(department=dept_id) | Q(course=course_id))
            notification.recievers.add(*receivers)
            notification.save()
            subject.notify(request, "Request sent")
    return redirect('lec_slides', dept_id, course_id, fac_id)


# Update Note
def update_note(request, dept_id, course_id, fac_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note_name = request.POST.get('noteName')
        note_content = request.FILES.get('noteContent')
        if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
            if note_name:
                note.name = note_name
            if note_content:
                note.content = note_content
            note.save()
            subject.notify(request, "Note has been updated")
        else:
            # Creating a temporary Note and sending notification
            temp_note = temp_Note.objects.create(name=note_name, content=note_content, faculty=note.faculty)
            notification = Notification.objects.create(
                message=f"{request.user.first_name} {request.user.last_name} wants to update a note",
                sender=request.user,
                type="update",
                content_type="note",
                content_id=temp_note.id,
                real_content_id=note.id
            )
            receivers = User.objects.filter(Q(role='master') | Q(department=dept_id) | Q(course=course_id))
            notification.recievers.add(*receivers)
            notification.save()
            subject.notify(request, "Request sent")
    return redirect('lec_notes', dept_id, course_id, fac_id)


# Update Video
def update_video(request, dept_id, course_id, fac_id, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video_name = request.POST.get('videoName')
        video_content = request.FILES.get('videoContent')
        if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
            if video_name:
                video.name = video_name
            if video_content:
                video.content = video_content
            video.save()
            subject.notify(request, "Video has been updated")
        else:
            # Creating a temporary Video and sending notification
            temp_video = temp_Video.objects.create(name=video_name, content=video_content, faculty=video.faculty)
            notification = Notification.objects.create(
                message=f"{request.user.first_name} {request.user.last_name} wants to update a video",
                sender=request.user,
                type="update",
                content_type="video",
                content_id=temp_video.id,
                real_content_id=video.id
            )
            receivers = User.objects.filter(Q(role='master') | Q(department=dept_id) | Q(course=course_id))
            notification.recievers.add(*receivers)
            notification.save()
            subject.notify(request, "Request sent")
    return redirect('lec_videos', dept_id, course_id, fac_id)

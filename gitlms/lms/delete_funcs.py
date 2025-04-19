from django.shortcuts import redirect,redirect, get_object_or_404
from .models import *
from accounts.models import User
from django.contrib import messages
from .Observer import Subject ,MessageObserver
from notifications.models import Notification
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .queryProxy import QueryCacheProxy

messageObserver=MessageObserver()
subject=Subject()
subject.attach(messageObserver)


@login_required
def delete_dept(request,dept_id):
    if (request.user.role!='master')&(request.user.department!=dept_id):
        return redirect('illegalactivity')
    if request.user.role=='master':
        department = Department.objects.get(id=dept_id)
        department.delete()
        proxy=QueryCacheProxy(request.user)
        proxy.delete_departments_cache()
        subject.notify(request, "Department has been deleted")
    else:
        subject.notify(request, "Request Sent")
    
    return redirect('departments')

@login_required
def delete_course(request,dept_id,course_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
        return redirect('illegalactivity')
    department=get_object_or_404(Department,id=dept_id)
    course = get_object_or_404(Course, id=course_id)
    if((request.user.role=='master')or(request.user.department== dept_id)):
        course.delete()
        proxy=QueryCacheProxy(request.user)
        proxy.delete_deptCourses_cache(department.id)
        subject.notify(request, "Course has been deleted")
    else:
        subject.notify(request, "Request Sent")
    return redirect('deptcourses',department.id)



@login_required
def delete_fac(request,dept_id,course_id,fac_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
         return redirect('illegalactivity')
    faculty=get_object_or_404(Faculty,id=fac_id)
    faculty.delete()
    proxy=QueryCacheProxy(request.user)
    proxy.delete_courseFacs_cache(faculty.course.department.id,faculty.course.id)
    subject.notify(request, "Faculty has been deleted")
    return redirect('course_facs',dept_id,course_id)



# Delete Slide
@login_required
def delete_slide(request, dept_id, course_id, fac_id, slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
        Notification.objects.filter(Q(real_content_id=slide.id)&Q(content_type="slide")).delete()
        slide.delete()
        proxy=QueryCacheProxy(request.user)
        proxy.delete_LecSlides_cache(slide.faculty.course.department.id,slide.faculty.course.id,slide.faculty.id)
        subject.notify(request, "Slide has been deleted")
    else:
       
        notification = Notification.objects.create(
            message=f"{request.user.first_name} {request.user.last_name} wants to delete a slide in {slide.faculty.course.department.name}/{slide.faculty.course.course_name}/{slide.faculty.name}",
            sender=request.user,
            type="delete",
            content_type="slide",
            real_content_id=slide.id
        )
        receivers = User.objects.filter(Q(role='master') | Q(department=dept_id) | Q(course=course_id))
        notification.recievers.add(*receivers)
        notification.save()
        subject.notify(request, "Request sent")

    return redirect('lec_slides', dept_id, course_id, fac_id)


# Delete Note
@login_required
def delete_note(request, dept_id, course_id, fac_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
        Notification.objects.filter(Q(real_content_id=note.id)&Q(content_type="note")).delete()
        note.delete()
        proxy=QueryCacheProxy(request.user)
        proxy.delete_LecNotes_cache(note.faculty.course.department.id,note.faculty.course.id,note.faculty.id)
        subject.notify(request, "Note has been deleted")
    else:
       
        notification = Notification.objects.create(
            message=f"{request.user.first_name} {request.user.last_name} wants to delete a note in {note.faculty.course.department.name}/{note.faculty.course.course_name}/{note.faculty.name}",
            sender=request.user,
            type="delete",
            content_type="note",
            real_content_id=note.id
        )
        receivers = User.objects.filter(Q(role='master') | Q(department=dept_id) | Q(course=course_id))
        notification.recievers.add(*receivers)
        notification.save()
        subject.notify(request, "Request sent")
    return redirect('lec_notes', dept_id, course_id, fac_id)


# Delete Video
@login_required
def delete_video(request, dept_id, course_id, fac_id, video_id):
    video = get_object_or_404(Video, id=video_id)
    if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
        Notification.objects.filter(Q(real_content_id=video.id)&Q(content_type="video")).delete()
        video.delete()
        proxy=QueryCacheProxy(request.user)
        proxy.delete_LecVideos_cache(video.faculty.course.department.id,video.faculty.course.id,video.faculty.id)
        subject.notify(request, "Video has been deleted")
    else:
        
        notification = Notification.objects.create(
            message=f"{request.user.first_name} {request.user.last_name} wants to delete a video in {video.faculty.course.department.name}/{video.faculty.course.course_name}/{video.faculty.name}",
            sender=request.user,
            type="delete",
            content_type="video",
            real_content_id=video.id
        )
        receivers = User.objects.filter(Q(role='master') | Q(department=dept_id) | Q(course=course_id))
        notification.recievers.add(*receivers)
        notification.save()
        subject.notify(request, "Request sent")
    return redirect('lec_videos', dept_id, course_id, fac_id)



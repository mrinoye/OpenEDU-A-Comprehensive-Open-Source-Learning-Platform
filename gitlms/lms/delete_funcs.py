from django.shortcuts import redirect,redirect, get_object_or_404
from .models import *
from accounts.models import User
from django.contrib import messages
from .Observer import Subject ,MessageObserver
from notifications.models import Notification
from django.db.models import Q


messageObserver=MessageObserver()
subject=Subject()
subject.attach(messageObserver)



def delete_dept(request,dept_id):
    if (request.user.role!='master')&(request.user.department!=dept_id):
        return redirect('illegalactivity')
    if request.user.role=='master':
        department = Department.objects.get(id=dept_id)
        department.delete()
        subject.notify(request, "Department has been deleted")
    else:
        subject.notify(request, "Request Sent")
    
    return redirect('departments')

def delete_course(request,dept_id,course_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
        return redirect('illegalactivity')
    department=get_object_or_404(Department,id=dept_id)
    course = get_object_or_404(Course, id=course_id)
    if((request.user.role=='master')or(request.user.department== dept_id)):
        course.delete()
        subject.notify(request, "Course has been deleted")
    else:
        subject.notify(request, "Request Sent")
    return redirect('deptcourses',department.id)




def delete_fac(request,dept_id,course_id,fac_id):
    if (request.user.role!='master')and(request.user.department!= dept_id)and(request.user.course!= course_id):
         return redirect('illegalactivity')
    faculty=get_object_or_404(Faculty,id=fac_id)
    faculty.delete()
    subject.notify(request, "Faculty has been deleted")
    return redirect('course_facs',dept_id,course_id)



# Delete Slide
def delete_slide(request, dept_id, course_id, fac_id, slide_id):
    slide = get_object_or_404(Slide, id=slide_id)
    if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
        slide.delete()
        subject.notify(request, "Slide has been deleted")
    else:
       
        notification = Notification.objects.create(
            message=f"{request.user.first_name} {request.user.last_name} wants to delete a slide",
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
def delete_note(request, dept_id, course_id, fac_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
        note.delete()
        subject.notify(request, "Note has been deleted")
    else:
       
        notification = Notification.objects.create(
            message=f"{request.user.first_name} {request.user.last_name} wants to delete a note",
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
def delete_video(request, dept_id, course_id, fac_id, video_id):
    video = get_object_or_404(Video, id=video_id)
    if (request.user.role == 'master') or (request.user.department == dept_id) or (request.user.course == course_id):
        video.delete()
        subject.notify(request, "Video has been deleted")
    else:
        
        notification = Notification.objects.create(
            message=f"{request.user.first_name} {request.user.last_name} wants to delete a video",
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



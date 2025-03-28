from django.shortcuts import redirect ,redirect, get_object_or_404
from .models import *
from accounts.models import User





def update_dept(request, dept_id):
    if (request.user.role!='master'):
        return redirect('illegalactivity')
    department = get_object_or_404(Department, id=dept_id)
    print("hi")
    if request.method == 'POST':
        dept_name = request.POST.get('departmentName')
        dept_desc = request.POST.get('departmentDescription')
        dept_image = request.FILES.get('departmentImage')
        print(dept_name,dept_desc, dept_image)
        if dept_name:
            department.name = dept_name
        if dept_desc:
            department.description = dept_desc
        if dept_image:
            department.image= dept_image

        department.save()

        return redirect('departments')
    
    return redirect('departments')


def update_course(request,dept_id,course_id):
    return redirect('depa_course')

def update_fac(request,dept_id,course_id,fac_id):
   return redirect('course_facs')

def update_slide(request,dept_id,course_id,fac_id,slide_id):
    return redirect('lec_slides')

def update_note(request,dept_id,course_id,fac_id,note_id):
    return redirect('lec_notes')

def update_video(request,dept_id,course_id,video_id):
    return redirect('lec_videos')



from django.shortcuts import redirect

def add_dept(request,dept_id):
    return redirect('department')

def add_course(request,dept_id,course_id):
    return redirect('depa_course')

def add_fac(request,dept_id,course_id,fac_id):
   return redirect('course_facs')

def add_slide(request,dept_id,course_id,fac_id,slide_id):
    return redirect('lec_slides')

def add_note(request,dept_id,course_id,fac_id,note_id):
    return redirect('lec_notes')

def add_video(request,dept_id,course_id,video_id):
    return redirect('lec_videos')



from django.shortcuts import redirect

def update_dept(request,dept_id):
    return redirect('department')

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



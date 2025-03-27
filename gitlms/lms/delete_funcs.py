from django.shortcuts import redirect

def delete_dept(request,dept_id):
    return redirect('department')

def delete_course(request,dept_id,course_id):
    return redirect('depa_course')

def delete_fac(request,dept_id,course_id,fac_id):
   return redirect('course_facs')

def delete_slide(request,dept_id,course_id,fac_id,slide_id):
    return redirect('lec_slides')

def delete_note(request,dept_id,course_id,fac_id,note_id):
    return redirect('lec_notes')

def delete_video(request,dept_id,course_id,video_id):
    return redirect('lec_videos')




import os
def slide_upload_to(instance, filename):
    return os.path.join(
        'contents', 
        instance.faculty.course.department.name, 
        instance.faculty.course.course_name, 
        instance.faculty.name, 
        'slides', 
        filename
    )


# Temporary Models

def temp_slide_upload_to(instance, filename):
    return os.path.join(
        'contents', 
        instance.real.faculty.course.department.name, 
        instance.real.faculty.course.course_name, 
        instance.real.faculty.name, 
        'temp_slides', 
        filename
    )



def temp_video_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.real.faculty.course.department.name,
        instance.real.faculty.course.course_name,
        instance.real.faculty.name,
        'temp_videos',
        filename
    )




def temp_note_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.real.faculty.course.department.name,
        instance.real.faculty.course.course_name,
        instance.real.faculty.name,
        'temp_notes',
        filename
    )


def slide_upload_to(instance, filename):
    # Construct the file path dynamically based on the related Department, Course, and Faculty
    return os.path.join(
        'contents', 
        instance.faculty.course.department.name, 
        instance.faculty.course.course_name, 
        instance.faculty.name, 
        'slides', 
        filename
    )


    
def video_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.faculty.course.department.name,
        instance.faculty.course.course_name,
        instance.faculty.name,
        'videos',
        filename
    )



def note_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.faculty.course.department.name,
        instance.faculty.course.course_name,
        instance.faculty.name,
        'notes',
        filename
    )
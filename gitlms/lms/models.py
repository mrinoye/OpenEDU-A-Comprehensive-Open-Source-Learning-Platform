from django.db import models
import os
from django.conf import settings




class Department(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates a primary key
    name = models.CharField(max_length=255, unique=True)  # Unique name field
    image = models.ImageField(upload_to='images/department/', null=True,default='images/department/default.jpg')  
    description=models.TextField(max_length=255,default="The Department fosters innovative research and interdisciplinary collaboration, focusing on conceptual exploration and advanced academic problem-solving techniques.")
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Course(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates a primary key
    course_code = models.CharField(max_length=6, unique=True)  # Unique course code
    course_name = models.CharField(max_length=50)  # Course name
    course_description = models.TextField(
        default="This course provides a comprehensive overview of essential topics, methodologies, and concepts. Further details will be provided."
    )  # Description of the course
    department = models.ForeignKey('Department', related_name='courses', on_delete=models.CASCADE)  # Foreign key to Department
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_administered', blank=True)  # Many-to-many field for admins
    image = models.ImageField(upload_to='images/course/', null=True, default='images/course/default.jpg')  # Course image

    def __str__(self):
        return self.course_name

    
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', related_name='Faculty', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/faculty/', null=True,default='images/faculty/default.jpg')  
    position = models.CharField(max_length=100)
    moderators= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='faculty_moderated', blank=True)  # Many-to-many field for admins
    # Add other relevant fields

    def __str__(self):
        return self.name
    




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

class Slide(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='slides', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=slide_upload_to)  # Use the slide_upload_to function for dynamic upload path
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
def video_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.faculty.course.department.name,
        instance.faculty.course.course_name,
        instance.faculty.name,
        'videos',
        filename
    )

class Video(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=video_upload_to)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def note_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.faculty.course.department.name,
        instance.faculty.course.course_name,
        instance.faculty.name,
        'notes',
        filename
    )
    
class Note(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='notes', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=note_upload_to)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    



from django.db import models
import os
from .models import Faculty  # Make sure to import the real models


def slide_upload_to(instance, filename):
    return os.path.join(
        'contents', 
        instance.faculty.course.department.name, 
        instance.faculty.course.course_name, 
        instance.faculty.name, 
        'slides', 
        filename
    )

class Slide(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='slides', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=slide_upload_to)  # Use the slide_upload_to function for dynamic upload path
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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

class temp_Slide(models.Model):
    name = models.CharField(max_length=100)
    real = models.ForeignKey(Slide, related_name='temp_versions', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=temp_slide_upload_to)  # Use the slide_upload_to function for dynamic upload path
    last_updated = models.DateTimeField(auto_now=True)
    
    # Foreign Key to original Slide
    
    def __str__(self):
        return self.name


def temp_video_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.real.faculty.course.department.name,
        instance.real.faculty.course.course_name,
        instance.real.faculty.name,
        'temp_videos',
        filename
    )

class temp_Video(models.Model):
    name = models.CharField(max_length=100)
    real = models.ForeignKey(Video, related_name='temp_versions', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=temp_video_upload_to)
    last_updated = models.DateTimeField(auto_now=True)

    # Foreign Key to original Video
    

    def __str__(self):
        return self.name


def temp_note_upload_to(instance, filename):
    return os.path.join(
        'contents',
        instance.real.faculty.course.department.name,
        instance.real.faculty.course.course_name,
        instance.real.faculty.name,
        'temp_notes',
        filename
    )

class temp_Note(models.Model):
    name = models.CharField(max_length=100)
    real = models.ForeignKey(Note, related_name='temp_versions', on_delete=models.CASCADE, null=True, blank=True)

    content = models.FileField(upload_to=temp_note_upload_to)
    last_updated = models.DateTimeField(auto_now=True)

    # Foreign Key to original Note
  
    def __str__(self):
        return self.name

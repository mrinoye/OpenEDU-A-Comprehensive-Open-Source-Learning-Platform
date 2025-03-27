from django.db import models
import os
from django.conf import settings
from .contentUploadStratagy import *



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
    












import os
from django.db import models

# Slide Model (Base)
class Slide(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='slides', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=SlideUploadStrategy.get_upload_to)  # Basic upload path for slides
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Video Model (Base)
class Video(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=VideoUploadStrategy.get_upload_to)  # Basic upload path for videos
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Note Model (Base)
class Note(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', related_name='notes', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=NoteUploadStrategy.get_upload_to)  # Basic upload path for notes
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



# Temporary Slide Model
class temp_Slide(models.Model):
    name = models.CharField(max_length=100)
    real = models.ForeignKey(Slide, related_name='temp_versions', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=TempSlideUploadStrategy().get_upload_to)  # Using TempSlideUploadStrategy
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Temporary Video Model
class temp_Video(models.Model):
    name = models.CharField(max_length=100)
    real = models.ForeignKey(Video, related_name='temp_versions', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=TempVideoUploadStrategy().get_upload_to)  # Using TempVideoUploadStrategy
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Temporary Note Model
class temp_Note(models.Model):
    name = models.CharField(max_length=100)
    real = models.ForeignKey(Note, related_name='temp_versions', on_delete=models.CASCADE, null=True, blank=True)
    content = models.FileField(upload_to=TempNoteUploadStrategy().get_upload_to)  # Using TempNoteUploadStrategy
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name








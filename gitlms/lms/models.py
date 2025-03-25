from django.db import models
import os


class Department(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates a primary key
    name = models.CharField(max_length=255, unique=True)  # Unique name field
    image = models.ImageField(upload_to='images/department/', null=True,default='images/department/default.jpg')  
    description=models.TextField(max_length=255,default="The Department fosters innovative research and interdisciplinary collaboration, focusing on conceptual exploration and advanced academic problem-solving techniques.")
    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates a primary key
    course_code = models.CharField(max_length=6, unique=True)  # Unique course code
    course_name = models.CharField(max_length=50)  # Course name
    course_description = models.TextField(default="This course provides a comprehensive overview of essential topics, methodologies, and concepts. Further details will be provided.)  # Description of the course")
    department = models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE)  # Foreign key to Department
    image = models.ImageField(upload_to='images/course/', null=True,default='images/course/default.jpg')  
    def __str__(self):
        return self.course_name
    
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', related_name='Faculty', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/faculty/', null=True,default='images/faculty/default.jpg')  
    position = models.CharField(max_length=100)
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
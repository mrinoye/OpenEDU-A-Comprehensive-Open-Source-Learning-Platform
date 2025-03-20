from django.db import models



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
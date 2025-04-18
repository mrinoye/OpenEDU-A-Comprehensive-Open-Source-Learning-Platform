from django.core.cache import cache
from .models import *
from django.contrib.auth.decorators import login_required

class QueryCacheProxy:
    def __init__(self, user):
        self.user = user
    
    @login_required
    def get_departments(self):
        # Check if departments are already cached
        departments_cache_key = 'all_departments'
        departments = cache.get(departments_cache_key)
        print(departments)
        if not departments:
            print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
            departments = Department.objects.all().order_by('name')
            cache.set(departments_cache_key, departments, timeout=60*15)  # Cache for 15 minutes
            
        return departments
    @login_required
    def get_deptCourses(self,dept_id):
        department=Department.objects.get(id=dept_id)
        # Check if departments are already cached
        coursess_cache_key = f'department?{department.id}'
        courses = cache.get(coursess_cache_key)
        print(courses)
        if not courses:
            print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
            courses = Course.objects.filter(department=department).order_by('course_name')
            cache.set(coursess_cache_key, courses, timeout=60*15)  # Cache for 15 minutes
            
        return courses,department
    @login_required
    def get_courseFacs(self,dept_id,course_id):
        department=Department.objects.get(id=dept_id)
        course=Course.objects.get(id=course_id)
        
        faculties_cache_key = f'department?{department.id}/course?{course.id}'
        faculties = cache.get(faculties_cache_key)
        print(faculties)
        if not faculties:
            print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
            faculties = Faculty.objects.filter(course=course).order_by('name')
            cache.set(faculties_cache_key, faculties, timeout=60*15)  # Cache for 15 minutes
            
        return faculties,department,course
    
    @login_required
    def get_LecSlides(self,dept_id,course_id,fac_id):
        department=Department.objects.get(id=dept_id)
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=fac_id)
        Slides_cache_key = f'department?{department.id}/course?{course.id}/faculty?{faculty.id}/Lectures/Slides'
        slides = cache.get(Slides_cache_key)
        print(slides)
        #if not slides:
        print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
        slides = Slide.objects.filter(faculty=faculty).order_by('-id')
        cache.set(Slides_cache_key, slides, timeout=60*15)  # Cache for 15 minutes
            
        return slides,department,course,faculty
    
    @login_required
    def get_LecVideos(self,dept_id,course_id,fac_id):
        department=Department.objects.get(id=dept_id)
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=fac_id)
        Videos_cache_key = f'department?{department.id}/course?{course.id}/faculty?{faculty.id}/Lectures/Videos'
        videos = cache.get(Videos_cache_key)
        print(videos)
        #if not videos:
        print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
        videos = Video.objects.filter(faculty=faculty).order_by('-id')
        cache.set(Videos_cache_key, videos, timeout=60*15)  # Cache for 15 minutes
            
        return videos,department,course,faculty

   
    @login_required
    def get_LecNotes(self,dept_id,course_id,fac_id):
        department=Department.objects.get(id=dept_id)
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=fac_id)
        Notes_cache_key = f'department?{department.id}/course?{course.id}/faculty?{faculty.id}/Lectures/Notes'
        notes = cache.get(Notes_cache_key)
        print(notes)
        #if not notes:
        print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
        notes = Note.objects.filter(faculty=faculty).order_by('-id')
        cache.set(Notes_cache_key, notes, timeout=60*15)  # Cache for 15 minutes
            
        return notes,department,course,faculty


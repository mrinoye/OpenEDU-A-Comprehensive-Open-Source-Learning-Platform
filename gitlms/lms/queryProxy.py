from django.core.cache import cache
from .models import *
from django.contrib.auth.decorators import login_required

class QueryCacheProxy:
    def __init__(self, user):
        self.user = user
    
    @login_required
    def get_departments(self):
       
        departments_cache_key = 'all_departments'
        departments = cache.get(departments_cache_key)
        print(departments)
        if not departments:             
            print("not cached yet")
            
            departments = Department.objects.all().order_by('name')
            cache.set(departments_cache_key, departments, timeout=60*15)  # Cache for 15 minutes
            
        return departments
    @login_required
    def get_deptCourses(self,dept_id):
        department=Department.objects.get(id=dept_id)
        
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
        if not slides:
            print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
            slides = Slide.objects.filter(faculty=faculty).order_by('-id')
            cache.set(Slides_cache_key, slides, timeout=60*10)  # Cache for 15 minutes   
        return slides,department,course,faculty
    
    @login_required
    def get_LecVideos(self,dept_id,course_id,fac_id):
        department=Department.objects.get(id=dept_id)
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=fac_id)
        Videos_cache_key = f'department?{department.id}/course?{course.id}/faculty?{faculty.id}/Lectures/Videos'
        videos = cache.get(Videos_cache_key)
        print(videos)
        if not videos:
            print("not cached yet")
            
            videos = Video.objects.filter(faculty=faculty).order_by('-id')
            cache.set(Videos_cache_key, videos, timeout=60*10)  # Cache for 15 minutes
            
        return videos,department,course,faculty

   
    @login_required
    def get_LecNotes(self,dept_id,course_id,fac_id):
        department=Department.objects.get(id=dept_id)
        course=Course.objects.get(id=course_id)
        faculty=Faculty.objects.get(id=fac_id)
        Notes_cache_key = f'department?{department.id}/course?{course.id}/faculty?{faculty.id}/Lectures/Notes'
        notes = cache.get(Notes_cache_key)
        print(notes)
        if not notes:
            print("not cached yet")
            
            notes = Note.objects.filter(faculty=faculty).order_by('-id')
            cache.set(Notes_cache_key, notes, timeout=60*10) 
            
        return notes,department,course,faculty
    
    @login_required
    def delete_departments_cache(self):
        departments_cache_key = 'all_departments'
        cache.delete(departments_cache_key)
        print(f"Deleted cache for: {departments_cache_key}")

    @login_required
    def delete_deptCourses_cache(self, dept_id):
        coursess_cache_key = f'department?{dept_id}'
        cache.delete(coursess_cache_key)
        print(f"Deleted cache for: {coursess_cache_key}")

    @login_required
    def delete_courseFacs_cache(self, dept_id, course_id):
        faculties_cache_key = f'department?{dept_id}/course?{course_id}'
        cache.delete(faculties_cache_key)
        print(f"Deleted cache for: {faculties_cache_key}")

    @login_required
    def delete_LecSlides_cache(self, dept_id, course_id, fac_id):
        Slides_cache_key = f'department?{dept_id}/course?{course_id}/faculty?{fac_id}/Lectures/Slides'
        cache.delete(Slides_cache_key)
        print(f"Deleted cache for: {Slides_cache_key}")

    @login_required
    def delete_LecVideos_cache(self, dept_id, course_id, fac_id):
        Videos_cache_key = f'department?{dept_id}/course?{course_id}/faculty?{fac_id}/Lectures/Videos'
        cache.delete(Videos_cache_key)
        print(f"Deleted cache for: {Videos_cache_key}")

    @login_required
    def delete_LecNotes_cache(self, dept_id, course_id, fac_id):
        Notes_cache_key = f'department?{dept_id}/course?{course_id}/faculty?{fac_id}/Lectures/Notes'
        cache.delete(Notes_cache_key)
        print(f"Deleted cache for: {Notes_cache_key}")


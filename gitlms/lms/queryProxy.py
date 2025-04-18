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
    def get_courses(self,department):
        # Check if departments are already cached
        coursess_cache_key = f'department?{department.id}'
        courses = cache.get(coursess_cache_key)
        print(courses)
        if not courses:
            print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
            courses = Course.objects.filter(department=department).order_by('course_name')
            cache.set(coursess_cache_key, courses, timeout=60*15)  # Cache for 15 minutes
            
        return courses

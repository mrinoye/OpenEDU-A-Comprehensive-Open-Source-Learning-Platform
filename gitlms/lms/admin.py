from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)

admin.site.register(Course)

admin.site.register(Faculty)

admin.site.register(Slide)

admin.site.register(Video)

admin.site.register(Note)
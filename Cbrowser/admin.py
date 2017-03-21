from django.contrib import admin
from . models import * 
# Register your models here.

admin.site.register(department)
admin.site.register(course)
admin.site.register(prof)
admin.site.register(student)
admin.site.register(enrollments)
admin.site.register(links)
from django.contrib import admin
from .models import *

admin.site.register(User)

admin.site.register(College)

admin.site.register(Subjects)

class FacultyRoutineInline(admin.StackedInline):
    model = FacultiesRoutine
    extra = 0

class FacultiesAdmin(admin.ModelAdmin):
    inlines = [FacultyRoutineInline,]

admin.site.register(Faculties, FacultiesAdmin)

class StreamsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("streamname",)}
    
admin.site.register(Streams, StreamsAdmin)
from django.contrib import admin
from .models import *


class CollegeGroupsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("groupname",)}
    
admin.site.register(CollegeGroups, CollegeGroupsAdmin)

admin.site.register(Grouproutine)

class GroupbreaksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("breakname",)}
    
admin.site.register(Groupbreaks, GroupbreaksAdmin)

admin.site.register(Groupsubjects)

class GroupclassesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("classname",)}
    
admin.site.register(Groupclasses, GroupclassesAdmin)

admin.site.register(Groupsubjectfaculties)
admin.site.register(GroupSpecifiction)
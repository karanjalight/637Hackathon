from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'price', 'fee', 'seller', 'created_at',
        'updated_at',
    )
    readonly_fields = ('id',)


admin.site.register(Course, CourseAdmin)

admin.site.register(Company_Profile)
admin.site.register(Job_Description)
admin.site.register(Meeting)
admin.site.register(Project_Documentation)


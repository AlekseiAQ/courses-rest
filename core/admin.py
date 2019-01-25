from django.contrib import admin

from core.models import Student, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date")


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseRecordAdmin)

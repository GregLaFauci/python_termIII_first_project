from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'courses','student_picture', 'year_in_school')
    ordering = ('last_name',)
    search_fields = ('first_name', 'last_name', 'id')

admin.site.register(Student, StudentAdmin)
from django.contrib import admin
from .models import Course, Enrollment, Annoucement, Comment

# Register your models here.


class CourseAdmin(admin.ModelAdmin): # configuração do admin

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} #coloca automaticamente o slug(atalho)


admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Annoucement, Comment])
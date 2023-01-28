from django.contrib import admin
from course.models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_cat', 'course_name', 'course_des', 'course_author', 'course_author_img', 'course_learner', 'course_like', 'course_price', 'course_img')



admin.site.register(Course, CourseAdmin)
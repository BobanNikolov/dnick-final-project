from django.contrib import admin
from final_project.models import CourseChapter, TeacherCourse, StudentCourse, Chapter, Course, Teacher, Student


# Register your models here.


class ChapterAdmin(admin.ModelAdmin):
    pass


class CourseChapterAdmin(admin.StackedInline):
    model = CourseChapter
    extra = 0


class TeacherCourseAdmin(admin.StackedInline):
    model = TeacherCourse
    extra = 0


class StudentCourseAdmin(admin.StackedInline):
    model = StudentCourse
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseChapterAdmin]


class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeacherCourseAdmin]


class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentCourseAdmin]


admin.site.register(Chapter)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
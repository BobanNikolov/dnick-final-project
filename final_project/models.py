from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Chapter(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    chapter_name = models.CharField(max_length=50, null=True, blank=True)
    chapter_video = models.FileField(upload_to='chapter_videos', blank=True)


class Course(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    course_video = models.FileField(upload_to='course_videos', blank=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    cost = models.IntegerField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    course_test = models.FileField(upload_to='course_test', blank=True)


class Teacher(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50, null=True, blank=True)


class Student(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50, null=True, blank=True)


class CourseChapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)


class TeacherCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
from django.shortcuts import render, redirect

from final_project.models import TeacherCourse, Course, Teacher


def get_courses(request):
    currentTeacher = Teacher.objects.get(user__username=request.user.username)
    courses = []
    for course in TeacherCourse.objects.all():
        if course.teacher.id == currentTeacher.id:
            courses.append(course.id)
    qs = Course.objects.filter(id__in=courses)
    return qs


# Create your views here.

def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def loggedin(request):
    return render(request, "loggedin.html")


def teacherIndex(request):
    courses = get_courses(request)
    context = {"courses": courses}
    return render(request, "teacherIndex.html", context=context)


def studentIndex(request):
    return render(request, "studentIndex.html")


def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('teacherIndex')


def enrolled(request):
    return render(request, "enrolled.html")


def createNewCourse(request):
    return render(request, "createNewCourse.html")

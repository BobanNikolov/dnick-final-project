from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from final_project.models import TeacherCourse, Course, Teacher, Student, StudentCourse, ShoppingCart, \
    ShoppingCartCourse


# Create your views here.

def index(request):
    return render(request, "index.html")


def login_app(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                teacher = Teacher.objects.get(user__username=username)
                if teacher is not None:
                    login(request, user)
                    return redirect("/teacherIndex")
            except:
                student = Student.objects.get(user__username=username)
                if student is not None:
                    login(request, user)
                    return redirect("/studentIndex")
    return render(request, "login.html")


def logout_app(request):
    username = User.objects.get(username=request.user.username)
    if username != None:
        logout(request)
        return redirect(login_app)


def signup(request):
    if request.method == "POST":
        selectedOption = request.POST["signup-select"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        name = request.POST["name"]
        if selectedOption == "teacher":
            user = User.objects.create_user(username, email, password)
            Teacher.objects.create(user=user, teacher_name=name)
            return redirect("/login")
        elif selectedOption == "student":
            user = User.objects.create_user(username, email, password)
            Student.objects.create(user=user, student_name=name)
            return redirect("/login")
    return render(request, "signup.html")


def loggedin(request):
    return render(request, "loggedin.html")


def teacherIndex(request):
    if request.user.is_authenticated:
        teacher_courses = TeacherCourse.objects.filter(teacher__user__username=request.user.username)
        courses = list()
        for teacher_course in teacher_courses:
            courses.append(teacher_course.course)
        emptyList = list()
        context = {"courses": courses, "emptyList": emptyList}
        return render(request, "teacherIndex.html", context=context)
    else:
        return redirect(login_app)


def studentIndex(request):
    if request.user.is_authenticated:
        student_courses = StudentCourse.objects.filter(student__user__username=request.user.username)
        courses = list()
        for student_course in student_courses:
            courses.append(student_course.course)
        emptyList = list()
        context = {"courses": courses, "emptyList": emptyList}
        return render(request, "studentIndex.html", context=context)
    else:
        return redirect(login_app)


def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('teacherIndex')


def deleteCourseAsStudent(request, id):
    course = ShoppingCartCourse.objects.filter(shopping_cart__student__user__username=request.user.username)\
        .filter(course__id=id)
    course.delete()
    return redirect('shoppingCart')


def enrolled(request, id):
    students = StudentCourse.objects.filter(course__id=id)
    context = {"students": students}
    return render(request, "enrolled.html", context=context)


def createNewCourse(request):
    return render(request, "createNewCourse.html")


def continueLearning(request, id):
    return render(request, "continueLearning.html")


def chooseNewCourse(request):
    studentCoursesBelongingToStudent = StudentCourse.objects.filter(student__user__username=request.user.username)
    allCourses = Course.objects.all()
    coursesBelongingToStudent = list()
    for s in studentCoursesBelongingToStudent:
        coursesBelongingToStudent.append(s.course)
    coursesNotBelongingToStudent = list()
    for c in allCourses:
        if c not in coursesBelongingToStudent:
            coursesNotBelongingToStudent.append(c)
    emptyList = list()
    shoppingCart = ShoppingCartCourse.objects.filter(shopping_cart__student__user__username=request.user.username)
    coursesInShoppingCart = list()
    for c in shoppingCart:
        coursesInShoppingCart.append(c.course)
    context = {"courses": coursesNotBelongingToStudent, "emptyList": emptyList,
               "coursesInShoppingCart": coursesInShoppingCart}

    return render(request, "chooseNewCourse.html", context=context)


def enroll(request, id):
    course = Course.objects.get(id=id)
    student = Student.objects.get(user__username=request.user.username)
    shoppingCart = ShoppingCart.objects.filter(student=student).exists()
    if shoppingCart is False:
        ShoppingCart.objects.create(student=student)
    shoppingCart = ShoppingCart.objects.get(student=student)
    ShoppingCartCourse.objects.create(shopping_cart=shoppingCart, course=course)
    return redirect('chooseNewCourse')


def shoppingCart(request):
    if request.method == "POST":
        shoppingCart = ShoppingCartCourse.objects.filter(shopping_cart__student__user__username=request.user.username)
        student = Student.objects.get(user__username=request.user.username)
        for c in shoppingCart:
            StudentCourse.objects.create(student=student, course=c.course)
        ShoppingCart.objects.filter(student__user__username=request.user.username).delete()
        return redirect('studentIndex')
    shoppingCart = ShoppingCartCourse.objects.filter(shopping_cart__student__user__username=request.user.username)
    coursesInShoppingCart = list()
    for c in shoppingCart:
        coursesInShoppingCart.append(c.course)
    emptyList = list()
    context = {"emptyList": emptyList, "coursesInShoppingCart": coursesInShoppingCart}
    return render(request, "shoppingCart.html", context=context)

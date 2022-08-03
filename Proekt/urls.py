"""Proekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from final_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('login/', login_app, name="login_app"),
    path('signup/', signup, name="signup"),
    path('loggedin/', loggedin, name="loggedin"),
    path('studentIndex/', studentIndex, name="studentIndex"),
    path('teacherIndex/', teacherIndex, name="teacherIndex"),
    path('delete-item/<int:id>/', deleteCourse, name="delete-item"),
    path('createNewCourse/', createNewCourse, name="createNewCourse"),
    path('enrolled/<int:id>/', enrolled, name="enrolled"),
    path('continue_learning/<int:id>', continueLearning, name="continue_learning"),
    path('logout/', logout_app, name="logout"),
    path('chooseNewCourse/', chooseNewCourse, name="chooseNewCourse"),
    path('enroll/<int:id>', enroll, name="enroll"),
    path('shoppingCart/', shoppingCart, name="shoppingCart"),
    path('delete-course/<int:id>/', deleteCourseAsStudent, name="delete-course"),
]

from django.urls import path
from . import views
from internapp.views import TaskView
urlpatterns = [
    path("",views.SigninForm, name='signinpage'),
    path("login/",views.LoginForm,name='loginpage'),
    path("homepage/",views.HomePage,name='homepage'),
    path("logout/",views.logout,name='logoutpage'),
    path("attendpage/",views.AttendencePage,name='attendpage'),
    path("taskpage/",views.TaskView,name='taskpage'),
    path("task/", TaskView.as_view(),name='task'),
    path("taskform/",views.TaskUpdateView ,name='taskform'),

]


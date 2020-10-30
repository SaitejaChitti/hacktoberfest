
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('forgetpassword/',views.forgetpassword,name="forgetpassword"),
]

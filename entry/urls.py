from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerPage, name="register"),
    path('viewKebele/', views.viewKebele, name="viewKebele"),
    path('login', views.loginPage, name="login"),

    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('update-user', views.updateUser, name="update-user"),
    path('', views.home, name="home"),
    path('addKebele', views.addKebele, name="addKebele"),
    path('addResident', views.addResident, name="addResident"),
    path('userProfile',views.userProfile,name="userProfile")
    #   for Systemadmin



]

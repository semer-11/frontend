from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerPage, name="register"),
    path('viewKebele', views.viewKebele, name="viewKebele"),
    path('login', views.loginPage, name="login"),

<<<<<<< HEAD
    path('login', views.loginPage, name="loginPage"),
    path('logoutuser/', views.logout_User, name="logoutuser"),
    path('register/', views.registerPage, name="register"),
    path('viewKebele/', views.viewKebele, name="viewKebele"),
    path('login/', views.loginPage, name="login"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('dele/<str:id>/', views.dele, name="dele"),
    path('update-user/', views.updateUser, name="update-user"),
=======
    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('update-user', views.updateUser, name="update-user"),
>>>>>>> 0661e1ed26a0ec21f3384b1412714652afa12dee
    path('', views.home, name="home"),
    path('addKebele', views.addKebele, name="addKebele"),
    path('addResident', views.addResident, name="addResident"),

    #   for Systemadmin



]

from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('report_death', views.reportDeath, name="reportDeath"),
    path('report_birth', views.reportBirth, name="reportBirth"),
    path('report_marriage', views.reportMarriage, name="reportMarriage"),
    path('report_divorce', views.reportDivorce, name="reportDivorce"),

    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerPage, name="register"),
    path('viewKebele/', views.viewKebele, name="viewKebele"),
    path('view_death_report',views.viewDeathReport,name="viewDeathReport"),
    path('view_birth_report',views.viewBirthReport,name="viewBirthReport"),
    path('view_mariage_report',views.viewMarriageReport,name="viewMarriageReport"),
    path('view_divorce_report',views.viewDivorceReport,name="viewDivorceReport"),
    path('login', views.loginPage, name="login"),

    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('update-user', views.updateUser, name="update-user"),
    path('', views.home, name="home"),
    path('addKebele', views.addKebele, name="addKebele"),
    path('addResident', views.addResident, name="addResident"),

    #   for Systemadmin



]

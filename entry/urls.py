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
    path('register/', views.registerPage, name="register"),
    path('viewKebele/', views.viewKebele, name="viewKebele"),
    path('viewStaff/', views.viewStaff, name="viewStaff"),
    path('view_death_reports',views.viewDeathReports,name="viewDeathReports"),
    path('view_death_report/<str:pk>',views.viewDeathReport,name="viewDeathReport"),
    path('view_birth_reports',views.viewBirthReports,name="viewBirthReports"),
    path('view_birth_report/<str:pk>',views.viewBirthReport,name="viewBirthReport"),
    path('view_mariage_reports',views.viewMarriageReports,name="viewMarriageReports"),
    path('view_marriage_report/<str:pk>',views.viewMarriageReport,name="viewMarriageReport"),
    path('view_divorce_reports',views.viewDivorceReports,name="viewDivorceReports"),
    path('view_divorce_report/<str:pk>',views.viewDivorceReport,name="viewDivorceReport"),
    path('validate_divorce_report/<str:pk>',views.validateDivorceReport,name="validateDivorceReport"),
    path('validate_death_report/<str:pk>',views.validateDeathReport,name="validateDeathReport"),
    path('validate_marriage_report/<str:pk>',views.validateMarriageReport,name="validateMarriageReport"),
    path('validate_birth_report/<str:pk>',views.validateBirthReport,name="validateBirthReport"),
    #path('profile', views.userProfile, name="profile"),
    #path('updateProfile', views.updateProfile, name="updateProfile"),
    #path('update-user', views.updateUser, name="update-user"),
    path('editResident',views.editResident,name="editResident"),
    path('', views.home, name="home"),
    path('addKebele', views.addKebele, name="addKebele"),
    path('addResident', views.addResident, name="addResident"),
    path('userProfile', views.userProfile, name="userProfile"),
    #   for Systemadmin



]

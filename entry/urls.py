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
    path('validate_birth_report/<str:pk>',views.validateBirthReport,name="validateBirthReport"),
    path('viewDeathReports', views.viewDeathReports, name="viewDeathReports"),
    path('viewBirthReports', views.viewBirthReports, name="viewBirthReports"),
    path('viewMarriageReports', views.viewMarriageReports,
         name="viewMarriageReports"),
    path('view_divorce_report', views.viewDivorceReport, name="viewDivorceReport"),
    path('login', views.loginPage, name="login"),

    path('viewDeathReport/<str:report_id>',
         views.viewDeathReport, name="viewDeathReport"),
    path('viewMarriageReport/<str:report_id>',
         views.viewMarriageReport, name="viewMarriageReport"),
    path('viewBirthReport/<str:report_id>',
         views.viewBirthReport, name="viewBirthReport"),
    path('profile', views.userProfile, name="profile"),
    path('updateProfile', views.updateProfile, name="updateProfile"),
    path('update-user', views.updateUser, name="update-user"),
    path('', views.home, name="home"),
    path('addKebele', views.addKebele, name="addKebele"),
    path('addResident', views.addResident, name="addResident"),
    path('userProfile', views.userProfile, name="userProfile"),
    path('getResult/', views.getResult, name="getResult")
    #   for Systemadmin



]

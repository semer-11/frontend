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

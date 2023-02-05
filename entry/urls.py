from django.urls import path
from . import views


urlpatterns = [

    path('login', views.loginPage, name="loginPage"),
    path('logoutuser/', views.logout_User, name="logoutuser"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('update-user/', views.updateUser, name="update-user"),
    path('', views.home, name="home"),
    path('addKebele', views.addKebele, name="addKebele"),
    path('addResident', views.addResident, name="addResident"),



    #   for Systemadmin



]

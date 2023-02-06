from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from .models import User,Kebele


class Usermodel(UserAdmin):
    list_display= ('username','first_name','last_name','email')
    search_fields= ('first_name','username','user_type')
    list_per_page= 10



admin.site.register(User,Usermodel) 
admin.site.register(Kebele)   
=======
from .models import Resident
# Register your models here.

admin.site.register(Resident)

>>>>>>> 0661e1ed26a0ec21f3384b1412714652afa12dee

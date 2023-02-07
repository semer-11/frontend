from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  User
import uuid


class Kebele(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    kebele_name = models.CharField(help_text=_("Required"), max_length=255, unique=True, blank=False)
    location = models.CharField(_("City"), max_length=150,help_text=_("Required"), null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Kebele")
        verbose_name_plural = _("Kebeles")

    def __str__(self):
        return self.kebele_name
        
GENDER = (
    ("Male","Male"),
    ("Faleme","Famele"),
    ("other","other"),
)

class Profile(models.Model):
    user=models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    kebele_name=models.ForeignKey(Kebele,on_delete=models.CASCADE,null=True,blank=True)
    gender = models.CharField(max_length=50,choices=GENDER,default="Male")
    role=models.IntegerField(default=1,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

GENDER = (
    ("Male","Male"),
    ("Faleme","Famele"),
    ("other","other"),
)
CHOICES = (
    ("single", "single"),
    ("married", "married"),
    ("divorced", "divorced"),
)

class Resident(models.Model):
    Resident_id=models.AutoField(primary_key=True)
    # Kebele_name=models.ForeignKey(kebele = models.ForeignKey(Kebele, null=True,on_delete = models.CASCADE))
    #admin = models.OneToOneField(User, on_delete = models.CASCADE)
    # registered_by=models.ForeignKey(User,blank=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50,choices=GENDER)
    Birth_date = models.CharField(max_length=20,null=True)
    phone = models.IntegerField(null=True)
    marital_status =models.CharField(max_length=20,choices=CHOICES)
    #image = models.ImageField(null=True, upload_to="img/%y") 
    No_of_Divorse=models.IntegerField(default=0)
    No_of_marrige=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    objects = models.Manager()

    class Meta:
        verbose_name = _("Resident")
        verbose_name_plural = _("Residents")


    def __str__(self):
        return self.first_name  
    

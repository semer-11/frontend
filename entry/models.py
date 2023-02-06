from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  User
import uuid

# Create your models here.
# class User(AbstractUser):
#     email=models.EmailField(max_length=200,null=True,blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     #id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
#     role=models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.username)


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
    admin = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50,choices=GENDER)
    Birth_date = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)
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
    
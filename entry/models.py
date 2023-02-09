from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  User
import uuid


class Kebele(models.Model):
    id=models.IntegerField(primary_key=True)
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
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

GENDER = (
    ("Male","Male"),
    ("Female","Female"),
)
CHOICES = (
    ("single", "single"),
    ("married", "married"),
    ("divorced", "divorced"),
)
STATUS = (
    ("alive", "alive"),
    ("dead", "dead"),
)


class Resident(models.Model):
    Resident_id=models.AutoField(primary_key=True)
    # Kebele_name=models.ForeignKey(kebele = models.ForeignKey(Kebele, null=True,on_delete = models.CASCADE))
    #admin = models.OneToOneField(User, on_delete = models.CASCADE)
    #approved_by=models.ForeignKey(User,blank=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=50,choices=GENDER)
    birth_date = models.DateField(max_length=200,null=True)
    birth_place = models.CharField(max_length=200,null=True)
    death_date = models.DateField(max_length=200,null=True)
    cause_of_death = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True)
    marital_status =models.BooleanField(max_length=20,choices=CHOICES,default="single")
    current_status=models.BooleanField(null=True,choices=STATUS,blank=True,default="alive")
    profile_image=models.ImageField(null=True,blank=True,upload_to='residents/',default='profiles/user-default.png')
    no_of_divorce=models.IntegerField(default=0)
    no_of_marriage=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    objects = models.Manager()

    class Meta:
        verbose_name = _("Resident")
        verbose_name_plural = _("Residents")


    def __str__(self):
        return self.first_name  
    
class reported_birth(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    for_kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE,max_length=50,null=True)
    birth_date = models.DateField(max_length=200,null=True)
    birth_place = models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=50,choices=GENDER)
    birth_proof=models.ImageField(null=True,blank=True,upload_to='proofs/')

    def __str__(self):
        return self.first_name

class reported_death(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    for_kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE,max_length=50,null=True)
    death_date = models.DateField(max_length=200,null=True)
    cause_of_death = models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    death_proof=models.ImageField(null=True,blank=True,upload_to='proofs/')

    def __str__(self):
        return self.first_name

class reported_marriages(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name_hus = models.CharField(max_length=50,null=True)
    last_name_hus = models.CharField(max_length=50,null=True)
    first_name_wife = models.CharField(max_length=50,null=True)
    last_name_wife = models.CharField(max_length=50,null=True)
    marriage_date= models.DateField(max_length=200,null=True)
    for_kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE,max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    marriage_proof=models.ImageField(null=True,blank=True,upload_to='proofs/')

    def __str__(self):
        return self.first_name_hus+self.first_name_wife
    
class reported_divorces(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name_hus = models.CharField(max_length=50,null=True)
    last_name_hus = models.CharField(max_length=50,null=True)
    first_name_wife = models.CharField(max_length=50,null=True)
    last_name_wife = models.CharField(max_length=50,null=True)
    for_kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE,max_length=50,null=True)
    divorce_date= models.DateField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    divorce_proof=models.ImageField(null=True,blank=True,upload_to='proofs/')

    def __str__(self):
        return self.first_name_hus+self.first_name_wife
    



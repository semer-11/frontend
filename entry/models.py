from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, User
from django.core.files.storage import FileSystemStorage




class User(AbstractUser):
        is_resident = models.BooleanField(default=False)
        is_systemadmin = models.BooleanField(default=False)
        is_KebeleEmployee = models.BooleanField(default=False)


       

class Kebele(models.Model):
    id = models.AutoField(primary_key=True)
    kebele_name = models.CharField(help_text=_("Required"), max_length=255, unique=True, blank=False)
    location = models.CharField(_("City"), max_length=150,help_text=_("Required"), null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    class Meta:
        verbose_name = _("Kebele")
        verbose_name_plural = _("Kebeles")

    def __str__(self):
        return self.kebele_name

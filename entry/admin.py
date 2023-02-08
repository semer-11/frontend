from django.contrib import admin
from .models import Resident,Kebele,Profile,reported_marriages,reported_birth,reported_death,reported_divorces
# Register your models here.

admin.site.register(Resident)
admin.site.register(Kebele)
admin.site.register(Profile)
admin.site.register(reported_marriages)
admin.site.register(reported_birth)
admin.site.register(reported_death)
admin.site.register(reported_divorces)


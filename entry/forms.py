
from django.forms import ModelForm
from entry.models import Resident

class ResidentForm(ModelForm):
       class Meta:
        model = Resident
        fields = '__all__'
        exclude = ['is_active','']

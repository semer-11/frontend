
from django.forms import ModelForm,widgets
from entry.models import Resident,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
       class Meta:
              model = User
              fields = ['first_name','email','username','password1','password2']
              labels = {
                     'first_name':'Name',
              }
       def __init__(self,*args,**kwargs):
              super(CustomUserCreationForm,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class ResidentForm(ModelForm):
       class Meta:
        model = Resident
        fields = '__all__'
        exclude = ['']
       
       def __init__(self,*args,**kwargs):
              super(ResidentForm,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class ProfileForm(ModelForm):
       class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['']

       def __init__(self,*args,**kwargs):
              
              super(ProfileForm,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

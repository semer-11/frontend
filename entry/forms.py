
from django.forms import ModelForm,widgets
from entry.models import Resident,Profile,reported_birth,reported_death,reported_divorces,reported_marriages
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
              exclude = ['death_date','cause_of_death','current_status''death_date','no_of_marriage','no_of_divorce']
       
       def __init__(self,*args,**kwargs):
              super(ResidentForm,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class ProfileForm(ModelForm):
       class Meta:
              model = Profile
              fields = '__all__'
              exclude = ['user']

       def __init__(self,*args,**kwargs):
              
              super(ProfileForm,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class Reported_death_Form(ModelForm):
       class Meta:
              model = reported_death
              fields = '__all__'
              exclude = ['id']
       
       def __init__(self,*args,**kwargs):
              super(Reported_death_Form,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class Reported_birth_Form(ModelForm):
       class Meta:
              model = reported_birth
              fields = '__all__'
              exclude = ['id']
       
       def __init__(self,*args,**kwargs):
              super(Reported_birth_Form,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class Reported_marriage_Form(ModelForm):
       class Meta:
              model = reported_marriages
              fields = '__all__'
              exclude = ['id']
       
       def __init__(self,*args,**kwargs):
              super(Reported_marriage_Form,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

class Reported_divorce_Form(ModelForm):
       class Meta:
              model = reported_divorces
              fields = '__all__'
              exclude = ['id']
       
       def __init__(self,*args,**kwargs):
              super(Reported_divorce_Form,self).__init__(*args,**kwargs)
              for name,fields in self.fields.items():
                     fields.widget.attrs.update({'class':'form-control '})

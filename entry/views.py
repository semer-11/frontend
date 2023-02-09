from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from entry.forms import ResidentForm,ProfileForm,CustomUserCreationForm,Reported_death_Form,Reported_birth_Form,Reported_marriage_Form,Reported_divorce_Form
from django.contrib import messages
from .models import Kebele,Profile,reported_birth,reported_death,reported_divorces,reported_marriages


def home(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            print("Username doesn't exist")
        authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print("Username or password incorrect")
    else:
        print("not even posted")

    return render(request, 'Pages/login.html')




def get_user_details(request):
    return HttpResponse("Please Login First")


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CustomUserCreationForm()
    #form_p= ProfileForm()
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
       # form_p= ProfileForm(request.POST) and form_p.is_valid()
        if form.is_valid() :
            user = form.save(commit=False)
            user.username=user.username.lower()
            #user.profile.user=request.user
            user.save()
            #profile = form_p.save(commit=False)
            #profile.user=user
            #print(profile.kebele_name)
            #profile.save(),'form_p':form_p
        else:
            print("THE SUMITTED DATA IS INVALID")
    else:
        print("something")
    context={'form':form}
    return render(request, 'Pages/register.html',context)

def viewKebele(request):
    kebeles = Kebele.objects.all()
    context = {
        "kebeles": kebeles
    }
    
    return render(request, 'Pages/viewKebele.html' ,context)
   
def viewDeathReport(request):
    reports = reported_death.objects.all()
    
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_death_report.html' ,context)
   
def viewBirthReport(request):
    reports = reported_birth.objects.all()
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_birth_report.html' ,context)


def viewMarriageReport(request):
    reports = reported_marriages.objects.all()
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_marriage_report.html' ,context)


def viewDivorceReport(request):
    reports = reported_divorces.objects.all()
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_divorce_report.html' ,context)

def userProfile(request):
    return render(request, 'Pages/Profile.html')

# @login_required(login_url='login')


def addKebele(request):
    
    if request.method == "POST":
        kebele = request.POST['kebelename']
        location = request.POST['location']
        try:
            kebele_model = Kebele(kebele_name=kebele, location=location) 
            kebele_model.save()
            messages.success(request, "Kebele Added Successfully!")
            return redirect('addKebele')
        except:
            messages.error(request, "Failed to Add Kebele!")
            return redirect('addKebele')
    
    return render(request, 'Pages/addKebele.html')


def addResident(request):
    form=ResidentForm()
    if request.method == "POST":
        #user = request.User
        form = ResidentForm(request.POST)
        try :
            form.is_valid()
            form.save()
            messages.success(request, "Resident is added successfully!!")
        except:
            print("Isnt valid")
        return redirect('addResident')
    else:
        return render(request, 'Pages/addResident.html',{'form':form})

def updateUser(request):
    user = request.user
    form = ResidentForm(instance=user)
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account has been update ss!!")
            return redirect('user-profile', pk=user.id)
    return render(request, 'base/update-user.html', {'form': form})

def reportDeath(request):
    form=Reported_death_Form()
    context={'form':form}
    if request.method == "POST":
        user = request.user
        form = Reported_death_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident is added successfully!!")
        else:
            print("Isnt valid")
        return redirect('login')
    else:
        return render(request,'Pages/report_death.html',context)
    
def reportBirth(request):
    form=Reported_birth_Form()
    context={'form':form}
    if request.method == "POST":
        user = request.user
        form = Reported_birth_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident is added successfully!!")
        else:
            print("Isnt valid")
        return redirect('login')
    else:
        return render(request,'Pages/report_birth.html',context)
    
def reportMarriage(request):
    form=Reported_marriage_Form()
    context={'form':form}
    if request.method == "POST":
        user = request.user
        form = Reported_marriage_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident is added successfully!!")
        else:
            print("Isnt valid")
        return redirect('login')
    else:
        return render(request,'Pages/report_marriage.html',context)
    
def reportDivorce(request):
    form=Reported_divorce_Form()
    context={'form':form}
    if request.method == "POST":
        user = request.user
        form = Reported_divorce_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident is added successfully!!")
        else:
            print("Isnt valid")
        return redirect('login')
    else:
        return render(request,'Pages/report_divorce.html',context)
    


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from entry.forms import ResidentForm,ProfileForm,CustomUserCreationForm,Reported_death_Form,Reported_birth_Form,Reported_marriage_Form,Reported_divorce_Form
from django.contrib import messages
from .models import Kebele,Resident,Profile,reported_birth,reported_death,reported_divorces,reported_marriages
from django.db import models
from django.core.exceptions import ObjectDoesNotExist



@login_required(login_url='login')
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


@login_required(login_url='login')
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

@login_required(login_url='login')
def editResident(request, resident_id):
    if request.method == "GET":
        try:
            user = Resident.objects.get(Resident_id=resident_id)
            kebele = Kebele.objects.all()
            return render(request, "Pages/editResident.html", {"user": user, "kebele": kebele})
        except ObjectDoesNotExist:
            return render(request, "Pages/404.html")
    elif request.method == "POST":
        kebele = Kebele.objects.get(id=request.POST['kebele_id'])
        user = Resident.objects.get(
            Resident_id=resident_id)
        # .update(Kebele_name=kebele)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.Kebele_name(id=kebele.id, kebele_name=kebele.kebele_name)
        user.save()
        return redirect("editResident")


# def updateUser(request):
#     user = request.user
#     form = ResidentForm(instance=user)
#     if request.method == 'POST':
#         form = ResidentForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your Account has been update ss!!")
#             return redirect('user-profile', pk=user.id)
#     return render(request, 'base/update-user.html', {'form': form})
# def updateProfile(request):
#     if request.method == "POST":
#         try:
#             if request.POST['email'] != "semer@gmail.com":
#                 raise ValidationError(
#                     f' {request.POST["email"]} no Valid email',
#                     params={'value': request.POST['email']},
#                 )
#             return render(request, "Pages/Profile.html")

#         except ValidationError as e:
#             return render(request, "Pages/Profile.html", {"error": e.message})
#     else:
#         return redirect("profile")


@login_required(login_url='login')
def viewKebele(request):
    kebeles = Kebele.objects.all()
    context = {
        "kebeles": kebeles
    }
    
    return render(request, 'Pages/viewKebele.html' ,context)


@login_required(login_url='login')
def viewStaff(request):
    staffs = User.objects.all()
    context = {
        "staffs": staffs
    }
    
    return render(request, 'Pages/viewStaff.html' ,context)


@login_required(login_url='login') 
def viewDeathReports(request):
    reports = reported_death.objects.all()
    
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_death_reports.html' ,context)


@login_required(login_url='login')
def viewDeathReport(request,pk):
    data = reported_death.objects.get(id=pk)
   
    
    return render(request, 'Pages/view_death_report.html' ,context={'data':data})


@login_required(login_url='login')
def viewBirthReports(request):
    reports = reported_birth.objects.all()
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_birth_reports.html' ,context)

@login_required(login_url='login')
def viewBirthReport(request,pk):
    data = reported_birth.objects.get(id=pk)
   
    
    return render(request, 'Pages/view_birth_report.html' ,context={'data':data})

@login_required(login_url='login')
def viewMarriageReports(request):
    reports = reported_marriages.objects.all()
    context = {
        "reports": reports
    }

    return render(request, 'Pages/view_marriage_reports.html' ,context)


@login_required(login_url='login')
def viewMarriageReport(request,pk):
    data = reported_marriages.objects.get(id=pk)
   
    
    return render(request, 'Pages/view_marriage_report.html' ,context={'data':data})


@login_required(login_url='login')
def validateDeathReport(request,pk):
    record=reported_death.objects.get(id=pk)
    resident=Resident.objects.get(first_name=record.first_name,last_name=record.last_name)
    resident.current_status="dead"
    resident.save()

    return redirect('viewDeathReports')



@login_required(login_url='login')
def validateBirthReport(request,pk):
    
    record=reported_birth.objects.get(id=pk)
    check=Resident.objects.get(first_name=record.first_name,last_name=record.last_name)
    record=reported_birth.objects.get(id=pk)
    if check.first_name != record.first_name: 
        resident=Resident.objects.create(
        first_name=record.first_name,
        last_name=record.last_name,
        birth_date=record.birth_date,
        birth_place=record.birth_place,
        kebele_name=record.for_kebele,
        gender=record.gender,
        )
        resident.save()
        record.is_visible=False
        record.save()
    else:
        print("dedeb")
            
    return redirect('viewBirthReports')

@login_required(login_url='login')
def validateMarriageReport(request,pk):
    record=reported_marriages.objects.get(id=pk)
    resident_h=Resident.objects.get(first_name=record.first_name_hus,last_name=record.last_name_hus)
    resident_h.marital_status="married"
    resident_h.save()
    resident_w=Resident.objects.get(first_name=record.first_name_wife,last_name=record.last_name_wife)
    resident_w.marital_status="married"
    resident_w.save()
    
    return redirect('viewMarriageReports')

@login_required(login_url='login')
def validateDivorceReport(request,pk):
    record=reported_divorces.objects.get(id=pk)
    resident_h=Resident.objects.get(first_name=record.first_name_hus,last_name=record.last_name_hus)
    resident_h.marital_status="divorced"
    resident_h.save()
    resident_w=Resident.objects.get(first_name=record.first_name_wife,last_name=record.last_name_wife)
    resident_w.marital_status="divorced"
    resident_w.save()
    
    return redirect('viewDivorceReports')



@login_required(login_url='login')
def viewDivorceReports(request):
    reports = reported_divorces.objects.all()
    context = {
        "reports": reports
    }
    
    return render(request, 'Pages/view_divorce_reports.html' ,context)


@login_required(login_url='login')
def viewDivorceReport(request,pk):
    data = reported_divorces.objects.get(id=pk)
   
    
    return render(request, 'Pages/view_divorce_report.html' ,context={'data':data})


@login_required(login_url='login')
def userProfile(request):
    return render(request, 'Pages/Profile.html')

# @login_required(login_url='login')


@login_required(login_url='login')
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


@login_required(login_url='login')
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


def reportDeath(request):
    form=Reported_death_Form()
    context={'form':form}
    if request.method == "POST":
        user = request.user
        form = Reported_death_Form(request.POST,request.FILES)
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
        form = Reported_birth_Form(request.POST,request.FILES)
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
    

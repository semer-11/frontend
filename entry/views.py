from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from entry.forms import ResidentForm,ProfileForm,CustomUserCreationForm
from django.contrib import messages
from .models import Kebele,Profile


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

    return render(request, 'Pages/login.html')




def get_user_details(request):
    return HttpResponse("Please Login First")


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CustomUserCreationForm()
    form_p= ProfileForm()
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        form_p= ProfileForm(request.POST)
        if form.is_valid & form_p.is_valid:
            user = form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            profile= form.save(commit=False)
            profile.save()
    context={'form':form,'form_p':form_p}
    return render(request, 'Pages/register.html',context)


def viewKebele(request):
    kebeles = Kebele.objects.all()
    context = {
        "kebeles": kebeles
    }
    
    return render(request, 'Pages/viewKebele.html' ,context)
   


def userProfile(request, pk):
    return render(request, 'base/profile.html')

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
        user = request.user
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident is added successfully!!")
        else:
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

    
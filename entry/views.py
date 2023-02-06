from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from entry.models import User, Kebele

from django.core import serializers
import json


=======
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from entry.forms import ResidentForm
from django.contrib import messages
>>>>>>> 0661e1ed26a0ec21f3384b1412714652afa12dee
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
    return render(request, 'Pages/register.html')


def viewKebele(request):
    kebeles = Kebele.objects.all()
    context = {
        "kebeles": kebeles
    }
    
    return render(request, 'Pages/viewKebele.html' ,context)
def dele(request,id):
    kebele = Kebele.objects.get(id=id)
    kebele.delete()
    return redirect(viewKebele)

    

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
    else:
        return render(request, 'Pages/addKebele.html')

     


def addResident(request):
    form=ResidentForm()
    if request.method == "POST":
        user = request.user
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resident is added successfully!!")
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

    
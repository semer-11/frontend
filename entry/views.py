from django.shortcuts import render, redirect
from django.http import HttpResponse
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


def home(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.method == "POST":
        return HttpResponse(request)
    else:

        return render(request, 'Pages/login.html')


def get_user_details(request):
    return HttpResponse("Please Login First")


def logout_User(request):
    return redirect('home')


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
    if request.method == "POST":
        return HttpResponse(request.POST['first_name'])
    else:
        return render(request, 'Pages/addResident.html')


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

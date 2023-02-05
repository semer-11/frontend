from django.shortcuts import render, redirect
from django.http import HttpResponse


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
    return render(request, 'base/login_register.html')


def userProfile(request, pk):
    return render(request, 'base/profile.html')

# @login_required(login_url='login')


def addKebele(request):
    if request.method == "POST":
        return HttpResponse(request)
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

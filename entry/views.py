from django.shortcuts import render, redirect
from django.http import HttpResponse




def home(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'base/login_register.html')

def get_user_details(request):
        return HttpResponse("Please Login First")

def logout_User(request):
    return redirect('home')


def registerPage(request):
    return render(request, 'Pages/register.html')

def viewKebele(request):
    return render(request,'Pages/viewKebele.html')
            
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request,user)
        messages.success(request, "Your Account has been activated!!")
        return redirect('update-user')
    else:
        return render(request,'activation_failed.html')

def userProfile(request, pk):
    return render(request, 'base/profile.html')

# @login_required(login_url='login')
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
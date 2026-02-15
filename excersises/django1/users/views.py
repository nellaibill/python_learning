from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm ,RegisterForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        print(form.errors)

    return render(request, "users/register.html", {"form": form})

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")

    return render(request, "users/login.html", {"form": form})             

@login_required
def home(request):
    
    print("Logged user:", request.user)
    print("User ID:", request.user.id)
    print("Profiles:", request.user.profiles.all())
    form = ProfileForm(request.POST or None)
    
    
    if request.method == "POST" and form.is_valid:
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect("home")
    profiles = request.user.profiles.all()
    return render(request, "users/home.html", {"form": form, "profiles": profiles})   



def user_logout(request):
    logout(request)
    return redirect("home")        



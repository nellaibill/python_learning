from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm

     

def home(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
            form = ProfileForm()
            
    users = Profile.objects.all()

    return render(request,"users/home.html",{"form": form,"users": users})

def edit_user(request,id):
    user = get_object_or_404(User,id=id)
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.save()
        return redirect("home")
    return render(request,"users/edit.html",{"user":user})

def delete_user(request,id):
    user = get_object_or_404(User,id=id)
    user.delete()
    return redirect("home")

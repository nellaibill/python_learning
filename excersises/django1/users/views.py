from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import UserForm,RegisterForm

def register(request):
    if(request.method =="POST"):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form =RegisterForm()
            
    return render(request,"users/register.html",{"form":form})        

def home(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
            form = UserForm()
            
    users = User.objects.all()

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

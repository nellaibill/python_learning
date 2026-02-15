from django import forms
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =['name','email','password1','password2']
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        
    def clean_name(self):
        name= self.cleaned_data.get("name") 
        if(len(name)<3):
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name
        
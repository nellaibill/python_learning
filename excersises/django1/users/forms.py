from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email']
        
    def clean_name(self):
        name= self.cleaned_data.get("name") 
        if(len(name)<3):
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name
        
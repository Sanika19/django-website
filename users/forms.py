from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    #class Meta gives us a nested namespace for configurations and keeps them in one place.
    #within the configurations we are stating that the model that will be affected is the user model.
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

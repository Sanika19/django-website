from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
#importing the "Login required" decorator:
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #to save user credentials to backend:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}! You can now log in.')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

#decorators add functionality to existing functions
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# types of messages
# debug
# info
# success
# etc

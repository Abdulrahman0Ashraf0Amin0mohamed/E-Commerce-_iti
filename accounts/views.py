from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            return redirect('library.home2')  
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})





@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('library.home')  
            else:
                return redirect('library.home2')  

    return render(request, 'registration/login.html')



def profile(request):
    user = request.user  

    if user is not None:
        login(request, user)
        if user.is_superuser:
            return redirect('library.home') 
        else:
            return redirect('library.home2') 
    else:
       
        return HttpResponse("You are not authenticated.")
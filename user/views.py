from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from .models import UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

def profile_view(request):
    return render(request, 'main/profile.html')

def Logout_view(request):
    logout(request)
    return redirect('home')

def Login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('todo_list')
            raise ValidationError('parol yoki username hato')   
    return render(request, 'main/login.html', context={
        'login_form':form,
    })

def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = UserModel(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=make_password(form.cleaned_data['password'])
            )
            user.save()
            return redirect('login')
    return render(request, 'main/registration.html', context={
        'registration_form': form,
    })

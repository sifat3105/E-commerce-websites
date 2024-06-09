from django.shortcuts import render, redirect
from auth_app.middlewares import not_verified_user
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from auth_app.models import profile

User = get_user_model()



#****************** Create your views here**********************
@not_verified_user
def home_view(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            return redirect('logout')
        log_reg = request.user.username
        log_reg_link = reverse('account')
    else:
        log_reg = 'Log In / Sign Up'
        log_reg_link = reverse('login_registration')
        
    return render(request, 'home.html',{'log_reg':log_reg, 'log_reg_link':log_reg_link})

def logout_view(request):
    logout(request)
    return redirect('login_registration')
@not_verified_user
def account(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            return redirect('logout')
    profile.objects.all()
    username = None
    if request.user.is_authenticated:
        log_reg = request.user.username
        log_reg_link = reverse('account')
        username = request.user.username
    else:
        log_reg = 'Log In / Sign Up'
        log_reg_link = reverse('login_registration')
    return render(request, 'profile.html',{'username':username, 'log_reg':log_reg, 'log_reg_link':log_reg_link,'Profile':profile})

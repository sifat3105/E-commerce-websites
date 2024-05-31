from django.shortcuts import render, redirect
from auth_app.middlewares import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import globals

User = get_user_model()



#****************** Create your views here**********************
def initialize_global_variables(request):
    if request.user.is_authenticated:
        globals.log_reg = request.user.username
        globals.username = request.user.username
        globals.log_reg_link = reverse('profile')
    else:
        globals.log_reg = 'Log In / Sign Up'
        globals.log_reg_link = reverse('login_registration')


@auth
def home_view(request):
    log_reg = globals.log_reg
    username = globals.username
    log_reg_link = globals.log_reg_link
   
        
    return render(request, 'home.html',{'log_reg':log_reg, 'log_reg_link':log_reg_link})

def logout_view(request):
    logout(request)
    return redirect('login_registration')

def profile(request):
    log_reg = globals.log_reg
    username = globals.username
    log_reg_link = globals.log_reg_link
    print(username)

    return render(request, 'profile.html', {'log_reg':log_reg, 'username':username, 'log_reg_link':log_reg_link, 'preloader':True})

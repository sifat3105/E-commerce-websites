from django.shortcuts import render, redirect
from auth_app.middlewares import not_verified_user
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from auth_app.models import profile
# from product.models import*

User = get_user_model()



#****************** Create your views here**********************

def home_view(request):
    
    return render(request, 'home.html')


@not_verified_user
def logout_view(request):
    logout(request)
    return redirect('login_registration')


@not_verified_user
def account(request):
    profile.objects.all()
   
    return render(request, 'profile.html',{'Profile':profile})

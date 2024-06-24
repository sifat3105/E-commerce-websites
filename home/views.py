from django.shortcuts import render, redirect
from auth_app.middlewares import not_verified_user
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from auth_app.models import profile
from .models import *
from django.contrib import messages
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

def billing_update(request):
    if request.method == 'POST':
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        
        # BillingAddress.objects.get_or_create(user=request.user)
        BillingAddress.objects.create(
        street_address = street_address,
        city = city,
        state = state,
        postal_code = zip_code,
        country = country,
        number = phone,
        user_id = request.user.id
        )
        messages.success(request, 'Billing Address Update Successfully')
        return redirect('account')
    return render(request, 'profile.html')
def shipping_update(request):
    if request.method == 'POST':
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        
        ShippingAddress.objects.create(
        street_address = street_address,
        city = city,
        state = state,
        postal_code = zip_code,
        country = country,
        number = phone,
        user_id = request.user.id
        )
        messages.success(request, 'Shipping Address Update Successfully')
        return redirect('account')
        
    return render(request, 'profile.html')
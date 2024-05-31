# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.core.mail import send_mail
from django.utils import timezone
from .models import Profile

def login_register_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = CustomAuthenticationForm(request, data=request.POST)
            register_form = CustomUserCreationForm()
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are now logged in as {username}.")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid login details.")
        elif 'register' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            login_form = CustomAuthenticationForm()
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.is_active = False
                user.save()
                profile = Profile.objects.create(user=user)

                profile.generate_otp()
                
                send_mail(
                    'Your OTP Code',
                    f'Click the link to verify your account: http://127.0.0.1:8000/auth/verify/{profile.otp}',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )
                messages.success(request, "An email has been sent to your address. Please verify your email to complete the registration.")
                
                # messages.success(request, "Registration successful.")
                return redirect('login_registration')
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        login_form = CustomAuthenticationForm()
        register_form = CustomUserCreationForm()

    return render(request, 'login_registration.html', {'login_form': login_form, 'register_form': register_form,'preloader':True})

def verify(request, otp):
    profile = get_object_or_404(Profile, otp=otp)
    if profile and profile.otp_is_valid():
        profile.is_verified = True
        profile.user.is_active = True
        profile.user.save()
        profile.save()
        messages.success(request, "Your account has been verified. You can now log in.")
        return redirect('/')
    else:
        messages.error(request, "Verification link is not valid or has expired.")
        return redirect('login_registration')
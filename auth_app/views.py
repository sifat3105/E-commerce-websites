from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import profile, forget_otp
from .middlewares import verified_user, not_verified_user
import random, re
from django.conf import settings
from django.utils.html import escape


@verified_user
def login_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            is_strong = False
            if re.search(r"[A-Z]+[a-z]+[0-9]+[!@#$%^&*(),/'.?:{}|<>]",password) and len(password) >7:
                is_strong = True
            if is_strong == False:
                messages.warning(request, 'Your password is weak.. ')
                return redirect('login_registration')
            else:
            
                if User.objects.filter(username =username).exists():
                    messages.warning(request, 'username  already exists')
                    return redirect('login_registration')
                elif User.objects.filter(email =email).exists():
                    messages.warning(request, 'email  already exists')
                    return redirect('login_registration')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.set_password(password)
                    user.save()
                    #for send otp
                    prof = profile.objects.create(user=user)
                    prof.generate_otp()
                    prof.save()
                    
                    html_message = f"""
                            <!DOCTYPE html>
                            <html>
                            <head>
                                <style>
                                    .button {{
                                        display: inline-block;
                                        padding: 10px 20px;
                                        font-size: 16px;
                                        cursor: pointer;
                                        text-align: center;
                                        text-decoration: none;
                                        outline: none;
                                        color: #fff;
                                        background-color: #4CAF50;
                                        border: none;
                                        border-radius: 15px;
                                        box-shadow: 0 9px #999;
                                    }}

                                    .button:hover {{background-color: #3e8e41}}

                                    .button:active {{
                                        background-color: #3e8e41;
                                        box-shadow: 0 5px #666;
                                        transform: translateY(4px);
                                    }}
                                </style>
                            </head>
                            <body>
                                <p>Click the button below to verify your account:</p>
                                <a href="http://127.0.0.1:8000/auth/verify/{escape(prof.otp)}" class="button">Verify Account</a>
                            </body>
                            </html>
                            """
                    send_mail(
                        'Your OTP Code',
                        f'Click the link to verify your account: http://127.0.0.1:8000/auth/verify/{prof.otp}',
                        'from@example.com',
                        [user.email],
                        fail_silently=False,
                        html_message = html_message,
                    )
                    messages.success(request, "An email has been sent to your address. Please verify your email to complete the registration.")
        else:
            messages.warning(request, 'password and confirm password does not match')
   
    if request.method == 'GET':
        username = request.GET.get('username_l')
        password = request.GET.get('password_l')
        user = authenticate(username=username, password=password)                                                                                                                                                                                                       
        if user:
            login(request, user)
            return redirect('home')          
    return render(request, 'login_registration.html', locals())

def verify(request, otp):
    prof = profile.objects.get(otp=otp)
    if prof:
        prof.is_verified = True
        prof.save()
        messages.success(request, "Your account has been verified. You can now log in.")
    else:
        messages.error(request, "Verification link is not valid or has expired.")
    return redirect('login_registration')

    
@not_verified_user
def details_update(request,id):
    data=User.objects.get(id=id)
    prof =profile.objects.get(user_id = id) 
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        display_name = request.POST.get('dname')
        number = request.POST.get('number')
        data.first_name=first_name
        data.last_name=last_name
        data.save()
        prof.display_name=display_name
        prof.phone_number=number
        prof.save()
        messages.success(request, f'{first_name} Your Account Details update successful.. ')
        return redirect('account')
    else:
        messages.warning(request, 'Your data is not valid..')
    
    return render(request, 'profile.html',locals())

@verified_user
def email_verifiation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Your search did not return any results. Please try again with other information.')
        else:
            generate_otp = random.randint(100000, 999999)
            forget_otp.objects.create(otp = generate_otp, email = email)
            subject = 'Your OTP Code'
            massage =f'Your OTP code is {generate_otp}. It is valid for 10 minutes.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, massage, email_from, recipient_list)
            return redirect('new_password')
           
    return render (request, 'email_verifiation.html')

@verified_user
def new_password(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user1 = forget_otp.objects.get(otp=otp)
        email = user1.email
        if forget_otp.objects.filter(otp = otp).exists():
            if password1 == password2:
                user2 = User.objects.get(email = email)
                username = user2.username
                user = get_user_model().objects.get(username=username)
                user.set_password(password1)
                user.save()
                user1.delete()
                return redirect('password_change_done')
            else:
                messages.error(request, 'New Password and confirm Confirm Password does not match.')
        else:
            messages.error(request,'otp', 'Invalid OTP')
    
    return render(request, 'change_pass.html',{'messages':messages})
      
def password_change_done(request):
    return render(request , 'password_change_done.html',)
        
@not_verified_user     
def reset_password(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        if new_password == confirm_new_password:
            user = get_user_model().objects.get(username=username)
            
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                send_mail(
                        'Password Change Successful',
                         'Hello {},\n\nYour password has been successfully changed.'.format(user.username),
                        'from@example.com',
                        [user.email],
                        
                    )
                messages.success(request, 'Your password was successfully updated!')
                return redirect('account')
            else:
                messages.warning(request, 'Old password is incorrect.')
        else:
            messages.warning(request, 'New Password and confirm Confirm Password does not match.')
                
    return render(request, 'profile.html')
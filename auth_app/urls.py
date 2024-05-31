from django.urls import path
from .views import login_register_view, verify

urlpatterns = [
    path('login_registration/', login_register_view, name='login_registration'),
    path('verify/<str:otp>/', verify, name='verify'),
]
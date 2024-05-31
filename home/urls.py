from django.urls import path
from .views import home_view, profile


urlpatterns = [
    path('', home_view , name='home'),
    path('profile/', profile, name='profile')
    
]

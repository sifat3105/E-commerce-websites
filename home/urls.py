from django.urls import path
from .views import home_view, account,logout_view


urlpatterns = [
    path('', home_view , name='home'),
    path('account/', account, name='account'),
    path('logout/', logout_view, name='logout')
    
]

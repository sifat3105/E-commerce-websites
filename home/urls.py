from django.urls import path
from .views import home_view, account,logout_view, shipping_update,billing_update


urlpatterns = [
    path('', home_view , name='home'),
    path('account/', account, name='account'),
    path('logout/', logout_view, name='logout'),
    path('billing_update/', billing_update, name='billing_update'),
    path('shipping_update/', shipping_update, name='shipping_update'),
    
]

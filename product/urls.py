from django.urls import path
from .views import create_product, product_view, right_product_view
urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('', product_view, name='product_view'),
    path('right_product_view/<str:uuid>', right_product_view, name='right_product_view'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
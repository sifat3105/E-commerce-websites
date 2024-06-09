from django.urls import path
from .views import create_product, product_view, upload_and_convert_image

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('', product_view, name='product_view'),
    path('upload/', upload_and_convert_image, name='upload_and_convert_image'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
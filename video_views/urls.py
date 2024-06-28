from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_videos, name='upload_video'),
    path('', views.video_list, name='video_list'),
]

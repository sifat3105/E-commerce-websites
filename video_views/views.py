from django.shortcuts import render, redirect
from django.urls import reverse
from .models import video

def upload_videos(request):
    if request.method == 'POST':
        youtube_url = request.POST.get(youtube_url)
        data=video.objects.create(youtube_url = youtube_url)
        data.save()
        
    return render(request, 'video/upload_video.html', locals())

def video_list(request):
    videos = video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos})

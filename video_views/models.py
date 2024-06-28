from django.db import models

class video(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

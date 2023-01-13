from django.db import models

# Create your models here.
class VideoData(models.Model):
    channelId = models.CharField(max_length=255, default=None)
    videoId = models.CharField(max_length=255, default=None)
    videoTitle = models.CharField(max_length=255, default=None)
    desc = models.CharField(max_length=255, default=None)
    channelTitle = models.CharField(max_length=255, default=None)
    pub_date = models.DateTimeField()
    thumb_url = models.URLField()
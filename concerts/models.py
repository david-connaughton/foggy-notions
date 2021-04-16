from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Concert(models.Model):
    presented_by = models.CharField(max_length=100,
                                    default="Foggy Notions")
    in_association_with = models.CharField(
        max_length=200, null=True, blank=True
    )
    artist = models.CharField(max_length=200, default="Artist")
    artist_one = models.CharField(max_length=200, null=True, blank=True)
    venue = models.CharField(max_length=100, default="Venue")
    date_one = models.DateField()
    date_two = models.DateField(null=True, blank=True)
    date_three = models.DateField(null=True, blank=True)
    original_date = models.DateField(null=True, blank=True)
    rescheduled_to = models.DateField(null=True, blank=True)
    rescheduled_to_1 = models.DateField(null=True, blank=True)
    rescheduled_to_2 = models.DateField(null=True, blank=True)
    time = models.TimeField()
    tickets = models.URLField(max_length=1024, null=True, blank=True)
    tickets_1 = models.URLField(max_length=1024, null=True, blank=True)
    tickets_2 = models.URLField(max_length=1024, null=True, blank=True)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = EmbedVideoField(null=True, blank=True)
    artist_website = models.URLField(max_length=1024, null=True, blank=True)
    artist_website_one = models.URLField(
        max_length=1024, null=True, blank=True)
    slug = models.SlugField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist

    class Meta:
        ordering = ['date_one']

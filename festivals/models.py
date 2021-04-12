from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Festival(models.Model):
    presented_by = models.CharField(max_length=100,
                                    default="Foggy Notions")
    in_association_with = models.CharField(
        max_length=200, null=True, blank=True
    )
    festival_name = models.CharField(max_length=200, default="Festival Name")
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    festival_website = models.URLField(
        max_length=1024, null=True, blank=True)
    festival_youtube = models.URLField(
        max_length=1024, null=True, blank=True)
    festival_facebook = models.URLField(
        max_length=1024, null=True, blank=True)
    festival_instagram = models.URLField(
        max_length=1024, null=True, blank=True)
    festival_twitter = models.URLField(
        max_length=1024, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.festival_name

    class Meta:
        ordering = ['date_start']

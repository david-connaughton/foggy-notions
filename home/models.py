from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    category = models.CharField(
        max_length=100, default="New Show Announcement")
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    more_info_link = models.URLField(max_length=1024, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted', ]

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

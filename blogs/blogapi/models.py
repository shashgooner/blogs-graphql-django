from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    comment = models.TextField()

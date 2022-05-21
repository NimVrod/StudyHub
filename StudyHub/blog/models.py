import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blog')
    posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Gallery(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    alt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.alt

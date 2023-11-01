from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=300, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateTimeField(default=datetime.now)
    online = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    content = models.TextField(max_length=300, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

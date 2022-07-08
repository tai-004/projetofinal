from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at =  models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    postar = models.BooleanField(default=False)
  

    def __str__(self):
        return self.title + "\n" + self.description
    class Meta:
         permissions = (("post", "post"),)

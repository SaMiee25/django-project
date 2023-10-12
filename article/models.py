from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null = True)
    description = models.TextField()
    image = models.ImageField(upload_to="post")
    other = models.ImageField(upload_to="post", default="")
    dateCreated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #CASCADE/RESTRICT



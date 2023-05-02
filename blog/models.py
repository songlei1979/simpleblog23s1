from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    post_image = models.ImageField(blank=True, null=True, upload_to="images/")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=str(self.id))

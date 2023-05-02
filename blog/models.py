from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", args=str(self.id))

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    post_image = models.ImageField(blank=True, null=True, upload_to="images/")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=str(self.id))

class Profile(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    web_page = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CreatePostForm
from blog.models import Post, Category, Profile


class home(ListView):
    model = Post
    template_name = "index.html"

class CategoryList(ListView):
    model = Category
    template_name = "category_list.html"

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class CategoryDetail(DetailView):
    model = Category
    template_name = "category_detail.html"

class PostCreate(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "post_create.html"
    # fields = "__all__"

class CategoryCreate(CreateView):
    model = Category
    template_name = "category_create.html"
    fields = "__all__"

class PostUpdate(UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = "post_update.html"
    # fields = "__all__"

class CategoryUpdate(UpdateView):
    model = Category
    fields = "__all__"
    template_name = "category_update.html"


class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("index")

class CategoryDelete(DeleteView):
    model = Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("category_list")

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    fields = "__all__"

class ProfileCreate(CreateView):
    model = Profile
    template_name = "profile_create.html"
    fields = "__all__"

class ProfileUpdate(UpdateView):
    model = Profile
    template_name = "profile_update.html"
    fields = ["address", "phone_number", "web_page"]

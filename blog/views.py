from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


class home(ListView):
    model = Post
    template_name = "index.html"

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreate(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = "__all__"

class PostUpdate(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = "__all__"

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("index")
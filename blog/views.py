from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CreatePostForm
from blog.models import Post, Category, Profile, Comment
import pandas as pd


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

def addComment(request):
    if request.method == "POST":
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        user = get_object_or_404(User, id=request.user.id)
        comment = request.POST.get('comment')
        if comment != "":
            Comment.objects.create(comment=comment, post=post, user=user)
        return HttpResponseRedirect(reverse('post_detail', args=[post.id]))

def like(request):
    if request.method == "POST":
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        user = get_object_or_404(User, id=request.user.id)
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return HttpResponseRedirect(reverse('post_detail', args=[post.id]))

def readExcelFile(request):
    if request.method == "POST" and request.FILES["myfile"]:
        myfile = request.FILES["myfile"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(filename)
        excel_data = pd.read_excel(myfile)
        data = pd.DataFrame(excel_data)
        usernames = data["username"].tolist()
        dobs = data["DOB"].tolist()
        firstnames = data["firstname"].tolist()
        lastnames = data["lastname"].tolist()
        emails = data["email"].tolist()
        addresses = data["address"].tolist()
        phone_numbers = data["phone_number"].tolist()
        web_pages = data["web_page"].tolist()
        i = 0
        while i < len(usernames):
            username = usernames[i]
            dob = dobs[i]
            firstname = firstnames[i]
            lastname = lastnames[i]
            email = emails[i]
            address = addresses[i]
            phone_number = phone_numbers[i]
            web_page = web_pages[i]
            m = dob.split("/")[0]
            d = dob.split("/")[1]
            y = dob.split("/")[2]
            if len(m) < 2:
                m = "0"+m
            if len(d) < 2:
                d = "0"+d
            password = m+d+y
            user = User.objects.create(username=username, password=password, first_name=firstname,
                                     last_name=lastname, email=email)
            profile = Profile.objects.create(user=user, address=address,phone_number=phone_number,web_page=web_page)
            user.groups.add(1)
            i = i + 1
        return render(request, 'upload_file.html', {
            "upload_file_url": upload_file_url
        })
    return render(request, 'upload_file.html')


def sendEmail(request):
    users = User.objects.all()
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        receiver = User.objects.get(id = request.POST.get("user"))
        senderEmail = "gabriel_sl19798@hotmail.com"
        try:
            send_mail(subject, body, senderEmail, [receiver.email],
                      fail_silently=False)
            return render(request, "emailsending.html", {
                "message": "email has been sent out",
                "users": users
            })
        except:
            return render(request, "emailsending.html", {
                "message": "email sending failed",
                "users": users
            })
    return render(request, "emailsending.html", {
        "message": "",
        "users": users
    })

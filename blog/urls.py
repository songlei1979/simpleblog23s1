from django.urls import path

from blog.views import home, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryDetail, CategoryCreate, \
    CategoryUpdate, CategoryDelete, CategoryList, ProfileDetail, ProfileCreate, ProfileUpdate

urlpatterns = [
    path("", home.as_view(), name="index"),
    path("post_detail/<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("post_create/", PostCreate.as_view(), name="post_create"),
    path("post_update/<int:pk>", PostUpdate.as_view(), name="post_update"),
    path("post_delete/<int:pk>", PostDelete.as_view(), name="post_delete"),
    path("category_detail/<int:pk>", CategoryDetail.as_view(), name="category_detail"),
    path("category_create/", CategoryCreate.as_view(), name="category_create"),
    path("category_update/<int:pk>", CategoryUpdate.as_view(), name="category_update"),
    path("category_delete/<int:pk>", CategoryDelete.as_view(), name="category_delete"),
    path("category_list/", CategoryList.as_view(), name="category_list"),
    path("profile_detail/<int:pk>", ProfileDetail.as_view(), name="profile_detail"),
path("profile_create/", ProfileCreate.as_view(), name="profile_create"),
path("profile_update/<int:pk>", ProfileUpdate.as_view(), name="profile_update"),

]
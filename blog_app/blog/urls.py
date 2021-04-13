from django.urls import path
from .views import BlogView, BlogDetailView, BlogCreatePost, BlogEditPost, BlogDeletePost

urlpatterns = [
    path('post/delete/<int:pk>/',BlogDeletePost.as_view(),name='delete_post' ),
    path('post/edit/<int:pk>/',BlogEditPost.as_view(),name='edit_post' ),
    path('post/new/',BlogCreatePost.as_view(),name='new_post' ),
    path('post/<int:pk>',BlogDetailView.as_view(), name= 'post_detail'),
    path('',BlogView.as_view(),name = 'home'),
]


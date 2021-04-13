from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blogs'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreatePost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'

class BlogEditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title','body']

class BlogDeletePost(DeleteView):
    model = Post
    template_name = 'delete_post_confirm.html'
    success_url = reverse_lazy('home')
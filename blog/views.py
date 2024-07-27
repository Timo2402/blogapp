from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    template_name = "home.html"
    
class PostDetail(DetailView):
    model = Post
    template_name = "detail.html"
    
class CreatePost(CreateView):
    model = Post
    fields = ["title","author","body"]
    template_name = "create.html"
    
    
class UpdatePost(UpdateView):
    model = Post
    fields = ["title","body"]
    template_name = "edit.html"
    
class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): # it return 'object or the lowercased name of our model'
    model = Post 
    template_name = 'Blog_detail.html'


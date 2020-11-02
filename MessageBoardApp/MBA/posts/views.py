from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.

# ListView return an object called 'object_list'
class HomePageView(ListView):
    model = Post
    template_name  = 'home.html' 
    context_object_name = 'all_post_list' # 'object_list' name changed to 'all_post_list'
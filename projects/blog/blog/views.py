from django.views.generic import ListView
from .models import Post

# Create your views here.

class BlogPostView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(ListView):
    model = Post
    template_name = "post_detail.html"
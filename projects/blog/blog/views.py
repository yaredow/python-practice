from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class BlogPostView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "blog_post"
    
from django.views.generic.list import ListView
from .models import Post

class PostListView(ListView):
    model = Post

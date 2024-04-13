from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic.list import ListView
from .models import Post

class HomeRedirectView(View):
    """A view that redirects the user to the list of posts.
    
    This view will be rendered when an empty path is requested from the server.
    """

    def get(self, _):
        """Redirects the user to the post list page."""
        return redirect(reverse("posts:index"))

class PostListView(ListView):
    model = Post

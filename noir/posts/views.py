from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
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
    """A view that shows all posts ordered by date (descending)."""
    model = Post
    context_object_name = "posts"
    ordering = "-created_at"

class PostCreateView(LoginRequiredMixin, CreateView):
    """A view that allows the user to create a new post.
    
    Authentication is required; additionally, the new post's creator field will
    be set to the currently authenticated user.
    """
    model = Post
    fields = ["title", "content"]
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

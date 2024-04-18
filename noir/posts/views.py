from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post, Reply


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
    paginate_by = 10
    ordering = "-created_at"
    template_name = "posts/post_list_page.html"

    def get_template_names(self, *args, **kwargs):
        return (
            "posts/post_list_body.html"
            if self.request.htmx and not self.request.htmx.boosted
            else self.template_name
        )


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
        self.object = form.save()
        res = HttpResponse()
        res.headers["HX-Redirect"] = form.instance.get_absolute_url()
        return res


class PostDetailView(DetailView):
    """A view that shows detailed information about a post.

    Information to be displayed includes title, content, timestamp and the reply
    tree."""

    model = Post
    context_object_name = "post"


class ReplyCreateView(LoginRequiredMixin, CreateView):
    """A view that allows the user to reply to a post."""

    model = Reply
    fields = ["post", "parent", "content"]
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        self.object = form.save()
        return render(
            self.request, "posts/components/reply.html", {"reply": form.instance}
        )

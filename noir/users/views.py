from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.detail import View
from .models import NUser


class UserProfileView(LoginRequiredMixin, View):
    """A view that shows information about the currently authenticated user.

    If the user is not logged in, they will be redirected to the login screen."""

    def get(self, request):
        """Renders a page showing information about the active user."""
        return render(request, "users/profile.html", {"user": request.user})

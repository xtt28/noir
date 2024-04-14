from django.urls.conf import path
from .views import HomeRedirectView, PostCreateView, PostDetailView, PostListView

# pylint:disable=all
app_name = "posts"

urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home"),
    path("posts/list", PostListView.as_view(), name="index"),
    path("posts/create", PostCreateView.as_view(), name="create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="detail"),
]

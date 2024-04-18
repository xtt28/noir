from django.urls.conf import path

from .views import (
    HomeRedirectView,
    PostCreateView,
    PostDetailView,
    PostListView,
    ReplyCreateView,
)

app_name = "posts"

urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home"),
    path("posts/list", PostListView.as_view(), name="index"),
    path("posts/create", PostCreateView.as_view(), name="create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="detail"),
    path("replies/create", ReplyCreateView.as_view(), name="reply_create"),
]

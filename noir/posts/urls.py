from django.urls.conf import path
from .views import PostListView

urlpatterns = [
    path("list", PostListView.as_view(), name="index"),
]

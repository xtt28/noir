from django.urls import path
from .views import UserProfileView

app_name = "users"

urlpatterns = [
    path("accounts/profile", UserProfileView.as_view(), name="profile"),
]

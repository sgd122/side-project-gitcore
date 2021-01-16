from django.urls import path
from . import views

urlpatterns = [
    path("users/<str:user_id>/", views.UserInfomationView.as_view(), name="user_info"),
    path("users/<str:user_id>/repo/", views.UserRepoView.as_view(), name="user_repo"),
]

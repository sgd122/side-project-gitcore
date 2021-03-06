from django.urls import path
from . import views

urlpatterns = [
    path("users/<str:user_id>/", views.UserInformationView.as_view(), name="user_info"),
    path("users/<str:user_id>/events/", views.UserEventsView.as_view(), name="user_events"),
    path("users/<str:user_id>/repos/", views.UserReposView.as_view(), name="user_repos"),
    path("users/<str:user_id>/today/", views.UserTodayView.as_view(), name="user_today"),
    path("repos/<str:user_id>/<str:repo>/", views.PullRequestView.as_view(), name="repo_pr"),
    path("repos/<str:user_id>/<str:repo>/<int:pull_number>/", views.GetPullRequestView.as_view(), name="repo_pr"),
    path("orgs/<str:org_id>/repos/", views.OrgsReposView.as_view(), name="org_repos"),
]

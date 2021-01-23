from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

app_name = "teams"

router = DefaultRouter()
router.register("", views.TeamViewSet)
router.register("", views.TeamGroupViewSet)

urlpatterns = router.urls

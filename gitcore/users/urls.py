from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

app_name = "users"

router = DefaultRouter()
router.register("", views.LoginViewSet)

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

app_name = "users"

router = DefaultRouter()
router.register("", views.LoginViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

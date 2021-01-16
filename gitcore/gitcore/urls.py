from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="side-project-gitcore",
      default_version='v1',
      description="[사이드프로젝트] Git Commit 예약 서비스",
      terms_of_service="https://github.com/sgd122/side-project-gitcore",
      contact=openapi.Contact(email="sgd0947@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("app/", include("app.urls")),
    path("users/", include("users.urls")),
]

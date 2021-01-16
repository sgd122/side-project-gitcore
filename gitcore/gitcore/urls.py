from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', get_swagger_view(title='API Docs')),
    path("app/", include("app.urls")),
    path("users/", include("users.urls")),
]

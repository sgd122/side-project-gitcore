from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users import views as users_views

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

urlSwaggerPatterns = [
    # Swagger
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlJwtPatterns = [
    # JWT
    path('api-jwt-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token),
    path('api-jwt-auth/verify/', verify_jwt_token),
]
urlOauthPatterns = [
    # Oauth
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # url(r'^complete/(?P<backend>[^/]+)/$', 'users.views.complete', name='complete'),
]

urlpatterns = urlSwaggerPatterns + \
              urlJwtPatterns + \
              urlOauthPatterns + \
              [
                  path('admin/', admin.site.urls),
                  # App
                  path("app/", include("app.urls")),
                  path("users/", include("users.urls")),
                  path("teams/", include("teams.urls")),
              ]

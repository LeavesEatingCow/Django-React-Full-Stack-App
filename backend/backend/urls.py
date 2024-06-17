from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView    #   Helps obtain access and refresh tokens and helps refresh tokens

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),   #   When we visit this site, it'll call the view method so we can create a new user
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),  
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from accounts.views import RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API 🚀"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # Auth endpoints
    path('api/auth/register/', RegisterView.as_view(), name="register"),
    path('api/auth/login/', TokenObtainPairView.as_view(), name="login"),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/auth/me/', UserDetailView.as_view(), name="me"),

    # Posts endpoints
    path('api/posts/', include("posts.urls")),   # <-- added this
]

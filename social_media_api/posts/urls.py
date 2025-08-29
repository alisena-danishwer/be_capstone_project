from django.urls import path, include

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    # Accounts
    path("api/auth/", include("accounts.urls")),

    # Posts
    path("api/posts/", include("posts.urls")),
]

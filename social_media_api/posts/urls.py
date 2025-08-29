# posts/urls.py
from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path("", PostListCreateView.as_view(), name="post-list-create"),   # /api/posts/
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),   # /api/posts/1/
]

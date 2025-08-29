# posts/views.py

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Post
from .serializers import PostSerializer


# List all posts or create a new one
class PostListCreateView(generics.ListCreateAPIView):
    """
    GET  -> List all posts
    POST -> Create a new post (requires login)
    """
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as author
        serializer.save(author=self.request.user)


# Retrieve, update, or delete a single post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    -> Retrieve a post by ID
    PUT    -> Update a post (only author can update)
    DELETE -> Delete a post (only author can delete)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Only allow the post's author to update
        if self.request.user == serializer.instance.author:
            serializer.save()
        else:
            raise PermissionDenied("❌ You can only update your own posts.")

    def perform_destroy(self, instance):
        # Only allow the post's author to delete
        if self.request.user == instance.author:
            instance.delete()
        else:
            raise PermissionDenied("❌ You can only delete your own posts.")

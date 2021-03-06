from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, PostUpdateSerializer
from .permissions import PostsPermissions


class PostsViewSet(ModelViewSet):
    """
    Post crud actions.

    Posts can be filtered by username ex: ```/api/posts?username=username-here```
    """
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [PostsPermissions]

    def get_queryset(self):

        # Filter by author's username if provided
        username = self.request.query_params.get('username')
        if username:
            return Post.objects.filter(author__username=username).order_by('-created_at')

        return self.queryset

    def perform_create(self, serializer):
        """Make sure the post is attached to the authorized user"""
        post = serializer.save(author=self.request.user)
        post.likes.add(self.request.user)
        return post

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return PostUpdateSerializer

        return PostSerializer

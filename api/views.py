from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from blogs.models import Posts, Comment
from .serializers import PostsDetailSerializer, PostsSerializer, CommentPostSerializer


class PostsListView(generics.ListAPIView):
    queryset = Posts.objects.all().prefetch_related('category')
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@method_decorator(vary_on_cookie)
@method_decorator(cache_page(60 * 60))
def dispatch(self, *args, **kwargs):
    return super(PostsListView, self).dispatch(*args, **kwargs)


class PostsCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Posts.objects.filter(id=self.kwargs['pk']).prefetch_related('category', 'comments')

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        comments_count = Comment.objects.filter(post=post).count()
        serializer = self.get_serializer(post)
        response_data = serializer.data
        response_data['comments_count'] = comments_count
        return Response(response_data)


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentPostSerializer

    def get_queryset(self):
        return Posts.objects.filter(id=self.kwargs['pk'])

    def post(self, request, pk):
        try:
            post = Posts.objects.get(id=pk)
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

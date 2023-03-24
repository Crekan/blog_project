from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostsListView.as_view(), name='posts'),
    path('post/create/', views.PostsCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/create/', views.CommentCreateView.as_view(), name='comment'),
]

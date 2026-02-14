from django.urls import path
from . import views

urlpatterns = [
    # Post CRUD URLs
    path('', views.PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # Post detail
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create new post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns += [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

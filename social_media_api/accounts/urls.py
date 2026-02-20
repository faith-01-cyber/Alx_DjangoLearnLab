from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]

from .views import PostViewSet, CommentViewSet, feed
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),  # feed endpoint
]

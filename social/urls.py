from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, follow_user, unfollow_user, feed_view

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
    path('feed/', feed_view),
]

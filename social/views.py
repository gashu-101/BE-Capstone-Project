from rest_framework import viewsets
from .models import Post, Follow
from .serializers import PostSerializer, FollowSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Attach user to the post


@api_view(['POST'])
def follow_user(request, user_id):
    followed = User.objects.get(id=user_id)
    if followed == request.user:
        return Response({'error': 'You cannot follow yourself.'}, status=400)
    
    Follow.objects.get_or_create(follower=request.user, followed=followed)
    return Response({'status': f'You are now following {followed.username}'})


@api_view(['POST'])
def unfollow_user(request, user_id):
    followed = User.objects.get(id=user_id)
    if followed == request.user:
        return Response({'error': 'You cannot unfollow yourself.'}, status=400)
    
    Follow.objects.filter(follower=request.user, followed=followed).delete()
    return Response({'status': f'You have unfollowed {followed.username}'})


@api_view(['GET'])
def feed_view(request):
    followed_users = request.user.following.values_list('followed_id', flat=True)
    posts = Post.objects.filter(Q(user__in=followed_users)).order_by('-timestamp')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

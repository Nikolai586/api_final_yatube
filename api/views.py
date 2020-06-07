# TODO:  Напишите свой вариант
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()



class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        if not self.request.query_params.get('group'):
            return Post.objects.all()
        return Post.objects.filter(group=self.request.query_params.get('group'))


class CommentViewSet(viewsets.ModelViewSet): 
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FollowList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=following__username', '=user__username']
    permission_classes = [IsAuthenticatedOrReadOnly] 

    def perform_create(self, serializer):
        following = User.objects.get(username=self.request.data.get('following'))
        user = self.request.user
        follow = Follow.objects.filter(user=user, following=following)
        if follow:
            raise ValidationError()
        return serializer.save(following=following, user=user)

    

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



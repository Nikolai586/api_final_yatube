from rest_framework import serializers

from .models import Post, Comment, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    following = serializers.CharField(source='following.username')
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title',)
        model = Group
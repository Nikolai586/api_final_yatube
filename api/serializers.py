from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, Comment, Follow, Group
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = ("id", "text", "author", "pub_date")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = ("id", "author", "post", "text", "created")
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    following = serializers.CharField(source="following.username")

    class Meta:
        fields = (
            "id",
            "user",
            "following",
        )
        model = Follow

    def validate(self, data):
        user = self.context["request"].user
        author = data["following"]
        follow_user = User.objects.get(username=author["username"])
        follow = Follow.objects.filter(user=user, following=follow_user)
        data["following"] = follow_user
        if follow:
            raise ValidationError()
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
        )
        model = Group

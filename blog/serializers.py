from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'author', 'publish', 'status', 'created', 'updated']


class PostShareSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    to = serializers.EmailField()
    comments = serializers.CharField()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = []

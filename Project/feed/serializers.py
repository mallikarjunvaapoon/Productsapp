from rest_framework import serializers
from .models import Feed, Comment

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('id', 'title', 'content', 'created_by', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_box')


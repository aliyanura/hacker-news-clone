from rest_framework import serializers
from .models import Story, Vote, Comment


class StorySerializer(serializers.ModelSerializer):
    """Serializer for story"""

    class Meta:
        model = Story
        fields = ("id", "title", "url", "created_at", "score", "created_by")
        extra_kwargs = {"created_by": {
            "default": serializers.CurrentUserDefault()
        }}


class StoryDetailSerializer(serializers.ModelSerializer):
    """Serializer for show story's detail with comments"""

    class Meta:
        model = Story
        fields = ("id", "title", "url", "created_at", "score", "created_by")
        extra_kwargs = {"created_by": {
            "default": serializers.CurrentUserDefault()
        }}

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["comments"] = CommentSerializer(
            instance.comments.all(), many=True
        ).data
        return representation


class VoteSerializer(serializers.ModelSerializer):
    """Serializer for votes"""

    class Meta:
        model = Vote
        fields = ("id", "story", "created_by")
        extra_kwargs = {"created_by": {
            "default": serializers.CurrentUserDefault()
        }}


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments"""

    class Meta:
        model = Comment
        fields = ("id", "message", "story", "created_by", "created_at")
        extra_kwargs = {"created_by": {
            "default": serializers.CurrentUserDefault()
        }}

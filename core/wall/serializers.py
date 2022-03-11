from rest_framework import serializers

from .models import WallPost


class WallPostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="name")
    likes = serializers.IntegerField(read_only=True, source="likes.count")

    class Meta:
        model = WallPost
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")


class WallLikeSerializer(serializers.ModelSerializer):
    wall_post = serializers.SlugRelatedField(read_only=True, slug_field="text")

    class Meta:
        model = WallPost
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")
